"""
Module: load_models.py
This module handles loading and storing the data fetched from Spotify into Django models.
"""
import os
import urllib.request
from django.conf import settings
from django.core.files import File
from products.models import Genre, Artist, Track, Album, ExternalUrl, Image
from .spotify_api import get_album_ids, get_album_details


def load_models(artist_name):
    """
    Function to load and store data fetched from Spotify into Django models.

    Parameters:
    - artist_name (str): The name of the artist to fetch data for.

    Returns:
    - None
    """
    album_ids = get_album_ids(artist_name)
    album_data = get_album_details(album_ids)

    for album_dict in album_data:
        artist_objs = []
        for artist_dict in album_dict.get("artists", []):
            artist, _ = Artist.objects.get_or_create(
                artist_name=artist_dict["name"],
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
                track_name=track_dict.get("name", "default_name"),
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

        # Break down Copyrights from Dictionary
        copyrights_list = album_dict.get(
            "copyrights", [{"text": "default_copyright"}]
        )
        if not copyrights_list:
            copyrights_list = [{"text": "default_copyright"}]
        first_copyright_text = copyrights_list[0]["text"]

        # Process the album data
        album, _ = Album.objects.get_or_create(
            album_name=album_dict.get("name", None),
            release_date=album_dict.get("release_date", None),
            total_tracks=album_dict.get("total_tracks", 0),
            popularity=album_dict.get("popularity", 0),
            artist_id=album_dict.get("artists", [{}])[0].get(
                "id", "default_artist_id"
            ),  # Retrieve artist_id
            album_id=album_dict.get("id", "default_id"),
            album_type=album_dict.get("album_type", "default_type"),
            label=album_dict.get("label", "default_label"),
            copyrights=first_copyright_text,
            # copyrights=album_dict.get("copyrights", "default_copyright"),
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
    """
    Function to convert duration into minutse and seconds.

    Parameters:
    duration_ms: The track duration (in milliseconds)

    Returns:
    f string: a String of the duration in minutes and seconds
    """
    minutes = duration_ms // 60000
    seconds = (duration_ms // 1000) % 60
    return f"{minutes}:{seconds:02d} mins"
