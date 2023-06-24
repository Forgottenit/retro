from products.models import Genre, Artist, Track, Album, ExternalUrl, Image
import os
import urllib.request
from django.conf import settings
from django.core.files import File
import requests
import base64
import time


def spotify_request(url, headers, params=None):
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 429:
            delay = int(response.headers.get("Retry-After"))
            time.sleep(delay)
        else:
            break

    data = response.json()

    # Pagination
    while data.get("next"):
        url = data.get("next")
        while True:
            response = requests.get(url, headers=headers)
            if response.status_code == 429:
                delay = int(response.headers.get("Retry-After"))
                time.sleep(delay)
            else:
                break

        data["items"].extend(response.json()["items"])

    return data


def get_auth_token():
    access_token = getattr(settings, "SPOTIFY_ACCESS_TOKEN", None)
    token_expiry_time = getattr(settings, "SPOTIFY_TOKEN_EXPIRY_TIME", None)

    if access_token and token_expiry_time > time.time():
        return access_token

    # Encode as Base64
    message = f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}"
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    headers = {
        "Authorization": f"Basic {base64_message}",
    }

    data = {
        "grant_type": "client_credentials",
    }

    response = requests.post(
        "https://accounts.spotify.com/api/token", headers=headers, data=data
    )

    access_token = response.json().get("access_token", None)
    token_expiry_time = time.time() + 3600 - 60  # 60 seconds safety margin

    # Store the access token and expiry time in settings
    setattr(settings, "SPOTIFY_ACCESS_TOKEN", access_token)
    setattr(settings, "SPOTIFY_TOKEN_EXPIRY_TIME", token_expiry_time)

    return access_token


artist_cache = {}


def get_artist_genres(artist_id):
    if artist_id in artist_cache:
        return artist_cache[artist_id]

    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    try:
        response = requests.get(
            f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error retrieving genres for artist {artist_id}: {e}")
        return []

    artist_data = response.json()

    if artist_data and "genres" in artist_data:
        genres = artist_data["genres"]
    else:
        genres = []

    artist_cache[artist_id] = genres
    return genres


def get_album_details(album_ids):
    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    albums_data = []

    for album_id in album_ids:
        try:
            response = requests.get(
                f"https://api.spotify.com/v1/albums/{album_id}",
                headers=headers,
            )
            response.raise_for_status()

            album_data = (
                response.json()
            )  # Assign the JSON response to album_data

            explicit = any(
                track.get("explicit", False)
                for track in album_data.get("tracks", {}).get("items", [])
            )
            album_data["explicit"] = explicit

            for artist in album_data.get("artists", []):
                artist_id = artist.get("id")
                if artist_id:
                    artist_genres = get_artist_genres(artist_id)
                    artist["genres"] = artist_genres
                    print("Genres TEST: ", artist["genres"])

            albums_data.append(album_data)
        except requests.RequestException as e:
            print(f"Failed to get album details for {album_id}. Error: {e}")
            continue

    return albums_data


def search_albums(query):
    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    params = (
        ("q", query),
        ("type", "album"),
    )

    response = requests.get(
        "https://api.spotify.com/v1/search", headers=headers, params=params
    )
    album_data = response.json().get("albums", {}).get("items", [])
    print(album_data)  # Print the album data for debugging

    return response.json()["albums"]["items"]


def get_album_ids(query):
    albums = search_albums(query)
    return [album["id"] for album in albums]


def load_models(artist_name):
    album_ids = get_album_ids(artist_name)
    album_data = get_album_details(album_ids)

    for album_dict in album_data:
        artist_objs = []
        for artist_dict in album_dict.get("artists", []):
            artist, _ = Artist.objects.get_or_create(
                name=artist_dict["name"],
                artist_id=artist_dict.get("id", "default_id"),
                spotify_url=artist_dict.get("external_urls", {}).get(
                    "spotify", "default_url"
                ),
                uri=artist_dict.get("uri", "default_uri"),
                type=artist_dict.get("type", "default_type"),
                href=artist_dict.get("href", "default_href"),
            )

            artist_objs.append(artist)
            # Handle the ExternalUrl for the artist
            external_urls_artist_dict = artist_dict.get("external_urls", {})
            external_url_artist, _ = ExternalUrl.objects.get_or_create(
                spotify=external_urls_artist_dict.get("spotify", "default_url")
            )
            artist.external_urls = external_url_artist

            # Process the genres for the artist
            genre_objs = set()
            for genre_name in artist_dict.get("genres", []):
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                genre_objs.add(genre)
            artist.genres.set(list(genre_objs))

            artist.save()
            artist_objs.append(artist)

        # Process the tracks for the album
        track_objs = []
        for track_dict in album_dict.get("tracks", {}).get("items", []):
            track_duration = format_duration(track_dict["duration_ms"])
            track, _ = Track.objects.get_or_create(
                track_number=track_dict.get("track_number", 0),
                name=track_dict.get("name", "default_name"),
                duration=track_duration,
                explicit=track_dict.get("explicit", False),
                spotify_url=track_dict.get("external_urls", {}).get(
                    "spotify", "default_url"
                ),
                uri=track_dict.get("uri", "default_uri"),
                type=track_dict.get("type", "default_type"),
                href=track_dict.get("href", "default_href"),
            )

            # Handle the ExternalUrl for the track
            external_urls_track_dict = track_dict.get("external_urls", {})
            external_url_track, _ = ExternalUrl.objects.get_or_create(
                spotify=external_urls_track_dict.get("spotify", "default_url")
            )
            track.external_urls = external_url_track
            track.save()

            for artist in artist_objs:
                track.artists.add(artist)
            track_objs.append(track)

            for genre_name in artist_dict.get("genres", []):
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                genre_objs.add(genre)

            for artist in artist_objs:
                track.artists.add(artist)
            track_objs.append(track)

        # Process the album data
        album, _ = Album.objects.get_or_create(
            album=album_dict.get("name", None),
            release_date=album_dict.get("release_date", None),
            total_tracks=album_dict.get("total_tracks", 0),
            popularity=album_dict.get("popularity", 0),
            artist_id=album_dict.get("artists", [{}])[0].get(
                "id", "default_artist_id"
            ),  # Retrieve artist_id
            album_id=album_dict.get("id", "default_id"),
            album_type=album_dict.get("album_type", "default_type"),
            label=album_dict.get("label", "default_label"),
            copyrights=album_dict.get("copyrights", "default_copyright"),
            explicit=album_dict.get("explicit", False),
            spotify_url=album_dict.get("external_urls", {}).get(
                "spotify", "default_url"
            ),
        )
        print("Genre Objects: ", genre_objs)
        print("Artist Objects: ", artist_objs)
        print("Track Objects: ", track_objs)

        # Add genres, artists, and tracks to the album
        album.genres.set(list(genre_objs))
        album.artists.set(artist_objs)
        album.tracks.set(track_objs)

        # Save the album image
        if album_dict["images"]:
            image_data = album_dict["images"][0]
            image_url = image_data["url"]
            image_height = image_data.get("height")
            image_width = image_data.get("width")
            album_id = album_dict["id"]
            image_filename = f"{album_id}.jpg"
            image_filepath = os.path.join(
                settings.MEDIA_ROOT, "album_images", image_filename
            )

            if not os.path.exists(image_filepath):
                urllib.request.urlretrieve(image_url, image_filepath)

            with open(image_filepath, "rb") as img_file:
                album.image.save(image_filename, File(img_file), save=False)

            # Save the image data in the Image model
            image_model, _ = Image.objects.get_or_create(
                url=image_url, height=image_height, width=image_width
            )
            album.image_data = image_model

        album.save()


def format_duration(duration_ms):
    minutes = duration_ms // 60000
    seconds = (duration_ms // 1000) % 60
    return f"{minutes}:{seconds:02d} mins"
