"""
Module: spotify_api.py
This module is responsible for interactions with Spotify API.

"""
import json
import base64
import time
import requests
from django.conf import settings


def get_auth_token():
    """
    Function to get the Spotify authentication token.

    Returns:
    - str: Access token if successful, None otherwise.
    """
    access_token = getattr(settings, "SPOTIFY_ACCESS_TOKEN", None)
    token_expiry_time = getattr(settings, "SPOTIFY_TOKEN_EXPIRY_TIME", None)
    # Token lasts one hour
    if access_token and token_expiry_time > time.time():
        return access_token

    # Encode as Base64 for security
    message = (
        f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}"
    )
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    headers = {
        "Authorization": f"Basic {base64_message}",
    }

    data = {
        "grant_type": "client_credentials",
    }

    try:
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            headers=headers,
            data=data,
            timeout=5,
        )
        response.raise_for_status()
        response_data = response.json()

        if "error" in response_data:
            error_status = (
                response_data["error"]["status"]
                if "status" in response_data["error"]
                else None
            )
            error_message = (
                response_data["error"]["message"] if error_status else None
            )
            error_description = (
                response_data["error_description"]
                if "error_description" in response_data
                else None
            )

            if error_status:  # Regular error object
                raise Exception(
                    f"Spotify API error {error_status}: {error_message}"
                )
            else:  # Authentication error object
                raise Exception(
                    f"Spotify API error: {response_data['error']}, "
                    f"Description: {error_description}"
                )
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"Error retrieving Spotify access token: {e}")
        return None

    access_token = response_data.get("access_token")
    if not access_token:
        print("Error: Access token not present in Spotify response")
        return None
    token_expiry_time = (
        time.time() + 3600 - 100
    )  # 3600 - token lasts 60 mins, so 60 mins - 100 seconds safety margin

    setattr(settings, "SPOTIFY_ACCESS_TOKEN", access_token)
    setattr(settings, "SPOTIFY_TOKEN_EXPIRY_TIME", token_expiry_time)

    return access_token


artist_cache = {}


def get_artist_genres(artist_id):
    """
    Function to get the genres of a specific artist by ID.

    Parameters:
    - artist_id (str): The Spotify ID of the artist.

    Returns:
    - list: List of genres if successful, otherwise empty list.
    """
    if artist_id in artist_cache:
        return artist_cache[artist_id]

    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    # Requesting artist data
    try:
        response = requests.get(
            f"https://api.spotify.com/v1/artists/{artist_id}",
            headers=headers,
            timeout=5,
        )
        response.raise_for_status()
        artist_data = response.json()

        if "error" in artist_data:
            error_status = (
                artist_data["error"]["status"]
                if "status" in artist_data["error"]
                else None
            )
            error_message = (
                artist_data["error"]["message"] if error_status else None
            )
            error_description = (
                artist_data["error_description"]
                if "error_description" in artist_data
                else None
            )

            if error_status:  # Regular error object
                raise Exception(
                    f"Spotify API error {error_status}: {error_message}"
                )
            else:  # Authentication error object
                raise Exception(
                    f"Spotify API error: {artist_data['error']}, "
                    f"Description: {error_description}"
                )
    except requests.RequestException as e:
        print("Error retrieving genres for artist {artist_id}: {e}")
        return []

    # Get genres from the artist data
    if artist_data and "genres" in artist_data:
        genres = artist_data["genres"]
    else:
        genres = []

    artist_cache[artist_id] = genres
    return genres


def get_album_details(album_ids):
    """
    Function to get the details of specific albums by their IDs.

    Parameters:
    - album_ids (list): The list of Spotify IDs of the albums.

    Returns:
    - list: List of album details if successful, otherwise empty list.
    """
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
                timeout=5,
            )
            response.raise_for_status()
            album_data = response.json()

            if "error" in album_data:
                error_status = (
                    album_data["error"]["status"]
                    if "status" in album_data["error"]
                    else None
                )
                error_message = (
                    album_data["error"]["message"] if error_status else None
                )
                error_description = (
                    album_data["error_description"]
                    if "error_description" in album_data
                    else None
                )

                if error_status:  # Regular error object
                    raise Exception(
                        f"Spotify API error {error_status}: {error_message}"
                    )
                else:  # Authentication error object
                    raise Exception(
                        f"Spotify API error: {album_data['error']}, "
                        f"Description: {error_description}"
                    )

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
        except requests.RequestException as e:
            print(f"Failed to get album details for {album_id}. Error: {e}")
            continue

    return albums_data


def search_albums(query, search_type="album", search_field="album"):
    """
    Function to search for albums on Spotify and retrieve their details.

    Parameters:
    - query (str): The search query to find albums on Spotify.
    - search_type (str): The type of search (default: "album").
    - search_field (str): The field to search for the query (default: "artist")

    Returns:
    - list: A list of album details if successful, an empty list otherwise.
    """

    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    # Search "Type" is Albums, if Artists returns list of Artists, not music
    params = (
        ("q", f"{search_field}:{query}"),
        ("type", search_type),
    )

    try:
        response = requests.get(
            "https://api.spotify.com/v1/search",
            headers=headers,
            params=params,
            timeout=5,
        )
        response.raise_for_status()
        album_data = response.json().get("albums", {}).get("items", [])

        if "error" in album_data:
            error_status = (
                album_data["error"]["status"]
                if "status" in album_data["error"]
                else None
            )
            error_message = (
                album_data["error"]["message"] if error_status else None
            )
            error_description = (
                album_data["error_description"]
                if "error_description" in album_data
                else None
            )

            if error_status:  # Regular error object
                raise Exception(
                    f"Spotify API error {error_status}: {error_message}"
                )
            else:  # Authentication error object
                raise Exception(
                    f"Spotify API error: {album_data['error']}, "
                    f"Description: {error_description}"
                )

    except requests.RequestException as e:
        print(f"Error retrieving albums for query '{query}': {e}")
        return []

    return album_data


def get_album_ids(query, search_field="artist"):
    """
    Function to retrieve the Spotify IDs of albums based on a search query.

    Parameters:
    - query (str): The search query to find albums on Spotify.
    - search_field (str): The field to search for the query (default: "artist")

    Returns:
    - list: A list of Spotify IDs of albums if successful,
      an empty list otherwise.
    """

    albums = search_albums(query, search_field=search_field)
    return [album["id"] for album in albums]
