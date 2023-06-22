import requests
import base64
from django.conf import settings
import json
import os
import urllib.request
from django.core.files import File


def get_auth_token():
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

    return response.json()["access_token"]


def get_artist_genres(artist_id):
    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(
        f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers
    )
    artist_data = response.json()

    if artist_data and "genres" in artist_data:
        genres = artist_data["genres"]
    else:
        genres = []

    return genres


def get_album_details(album_ids):
    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    albums_data = []

    for album_id in album_ids:
        response = requests.get(
            f"https://api.spotify.com/v1/albums/{album_id}", headers=headers
        )
        album_data = response.json()

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

        albums_data.append(album_data)

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
    album_data = response.json()["albums"]["items"]
    print(album_data)  # Print the album data for debugging

    return response.json()["albums"]["items"]


def get_album_ids(query):
    albums = search_albums(query)
    return [album["id"] for album in albums]


def format_duration(duration_ms):
    minutes = duration_ms // 60000
    seconds = (duration_ms // 1000) % 60
    return f"{minutes}:{seconds:02d}"


def create_fixtures(artist_name):
    album_ids = get_album_ids(artist_name)
    print("Album IDs:", album_ids)
    album_data = get_album_details(album_ids)
    print("Album Data:", album_data)
    try:
        with open("fixtures/album_fixtures.json", "r", encoding="utf-8") as f:
            try:
                fixtures = json.load(f)
            except json.JSONDecodeError as e:
                # Handle JSONDecodeError when the file is empty or contains invalid JSON
                print("Error occurred while decoding JSON response:", str(e))
                fixtures = []
    except FileNotFoundError:
        fixtures = []
    # Extract all existing album IDs in the fixtures
    existing_album_ids = {fixture["fields"]["id"] for fixture in fixtures}

    start_pk = len(fixtures)

    for i, album in enumerate(album_data, start=start_pk):
        # Skip if this album is already in the fixtures
        if album["id"] in existing_album_ids:
            continue

        # Filter the album data to remove "available_markets"
        album.pop("available_markets", None)

        # Filter the track data to remove "available_markets" and format duration
        for track in album["tracks"]["items"]:
            track.pop("available_markets", None)
            track["duration_ms"] = format_duration(track["duration_ms"])

        # Process album images
        album_images = []
        if album["images"]:
            # Get the first image data
            image_data = album["images"][0]

            # Get the image URL
            image_url = image_data["url"]

            # Extract the album ID
            album_id = album["id"]

            # Construct the file path and name
            image_filename = f"{album_id}.jpg"
            image_filepath = os.path.join(
                settings.MEDIA_ROOT, "album_images", image_filename
            )

            # Check if the image with the same ID already exists
            if not os.path.exists(image_filepath):
                # Download the image and save it to the media directory
                urllib.request.urlretrieve(image_url, image_filepath)

            # Add the image file to the album's images list
            album_images.append(image_filepath)

            # Update the album image URL to reference the saved image
            album["images"][0][
                "url"
            ] = f"{settings.MEDIA_URL}album_images/{image_filename}"

        # Add the album images to the album data
        album["album_images"] = album_images

        fixture = {
            "model": "products.album",  # Replace with your actual model
            "pk": i,
            "fields": album,
        }

        # Check if a fixture with the same album ID already exists
        existing_fixture = next(
            (
                f
                for f in fixtures
                if f["fields"]["id"] == fixture["fields"]["id"]
            ),
            None,
        )

        if existing_fixture:
            # Update the existing fixture with the new data
            existing_fixture["fields"] = fixture["fields"]
        else:
            # Add the new fixture to the list
            fixtures.append(fixture)

    with open("fixtures/album_fixtures.json", "w", encoding="utf-8") as f:
        json.dump(fixtures, f)
