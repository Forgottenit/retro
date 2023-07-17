"""
Module: load_models.py
This module handles loading and storing the data
fetched from Spotify into Django models.
https://developer.spotify.com/
https://www.youtube.com/watch?v=R-22NeS-P2c&ab_channel=TechWithTim
"""
import os
import urllib.request
from django.conf import settings
from django.core.files import File
from products.models import Genre, Artist, Track, Album
from .spotify_api import get_album_ids, get_album_details


def load_models(query, search_field="artist"):
    """
    Function to load and store data fetched from Spotify into Django models.

    Parameters:
    - query (str): The name of the artist to fetch data for.
    - search_field (str): The field to search for the query (default: "artist")
    - Type is set to Albums.
    - *This is because Spotify API search uses fields of Query,
      Type and Fields i.e. Query = "Beatles", Albums = Type ,
      Albums = Fields would search Beatles in Album names, and
      return Albums with the word Beatles in them. Beatles,
      Artists, Artists would search Artists for the word Beatles,
      and return the Artist. Beatles, Artists, Albums would search
      Artists for Beatles, and return Albums by the Artist Beatles.

    Returns:
    - None
    """

    album_ids = get_album_ids(query, search_field=search_field)
    album_data = get_album_details(album_ids)

    for album_dict in album_data:
        album_id = album_dict["id"]

        # Check if the album with the given ID already exists
        try:
            album = Album.objects.get(album_id=album_id)
            # If album exists, skip processing
            continue
        except Album.DoesNotExist:
            # Create a new album instance
            album = Album(album_id=album_id)

        for artist_dict in album_dict.get("artists", []):
            artist_objs = []
            artist, _ = Artist.objects.get_or_create(
                artist_name=artist_dict["name"],
                artist_id=artist_dict.get("id", "default_id"),
                spotify_url=artist_dict.get("external_urls", {}).get(
                    "spotify", "default_url"
                ),
                type=artist_dict.get("type", "default_type"),
                href=artist_dict.get("href", "default_href"),
            )

            artist_objs.append(artist)

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
                type=track_dict.get("type", "default_type"),
                href=track_dict.get("href", "default_href"),
            )

            track.save()

            for artist in artist_objs:
                track.artists.add(artist)
            track_objs.append(track)

            for genre_name in artist_dict.get("genres", []):
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                genre_objs.add(genre)

        # Break down Copyrights from Dictionary,
        # First one only taken
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
            ),  # Get artist_id
            album_id=album_dict["id"],
            album_type=album_dict.get("album_type", "default_type"),
            label=album_dict.get("label", "default_label"),
            copyrights=first_copyright_text,
            explicit=album_dict.get("explicit", False),
            spotify_url=album_dict.get("external_urls", {}).get(
                "spotify", "default_url"
            ),
        )

        # Add genres, artists, and tracks to the album
        # As a set to prevent duplication
        album.genres.set(list(genre_objs))
        album.artists.set(artist_objs)
        album.tracks.set(track_objs)

        # Save the album image
        if album_dict["images"]:
            image_data = album_dict["images"][0]
            image_url = image_data["url"]
            album_id = album_dict["id"]
            # image name is album id followed by .jpg
            image_filename = f"{album_id}.jpg"
            # image filepath set
            image_filepath = os.path.join(
                settings.MEDIA_ROOT, "album_images", image_filename
            )

            if not os.path.exists(image_filepath):
                urllib.request.urlretrieve(image_url, image_filepath)
            # Save image in Media folder
            with open(image_filepath, "rb") as img_file:
                album.image.save(image_filename, File(img_file), save=False)

        if artist_objs:
            album.main_artist = artist_objs[0]

        album.save()


def format_duration(duration_ms):
    """
    Function to convert duration into minutes and seconds.
    as format is seconds
    Parameters:
    - duration_ms (int): The track duration in milliseconds

    Returns:
    - A formatted string of the duration in minutes and seconds.
    """
    minutes = duration_ms // 60000
    seconds = (duration_ms // 1000) % 60
    return f"{minutes}:{seconds:02d} mins"
