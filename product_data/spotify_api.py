"""
Module: spotify_api.py
This module is responsible for interactions with Spotify API.
"""
import json
import base64
import time
import requests
from django.conf import settings


def spotify_request(url, headers, params=None):
    """
    Function to send a request to Spotify API and handle any errors.

    Parameters:
    url (str): URL of the Spotify API endpoint
    headers (dict): Request headers
    params (dict): Query parameters for the request

    Returns:
    dict: Response data from the Spotify API
    """
    # Main request handling loop
    while True:
        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=5
            )
            response.raise_for_status()

            data = response.json()
            if "error" in data:
                error_status = (
                    data["error"]["status"]
                    if "status" in data["error"]
                    else None
                )
                error_message = (
                    data["error"]["message"] if error_status else None
                )
                error_description = (
                    data["error_description"]
                    if "error_description" in data
                    else None
                )

                if error_status:  # Regular error object
                    raise Exception(
                        "Spotify API error {}: {}".format(
                            error_status, error_message
                        )
                    )
                else:  # Authentication error object
                    raise Exception(
                        "Spotify API error: {}, Description: {}".format(
                            data["error"], error_description
                        )
                    )
        except (requests.RequestException, json.JSONDecodeError):
            raise Exception(
                "Request failed or response does not contain valid JSON."
            )
        except Exception as e:
            print("An error occurred: {}".format(e))

        # Handling rate limits
        if response.status_code == 429:
            delay = int(response.headers.get("Retry-After"))
            time.sleep(delay)
        elif response.status_code != 200:  # if not success
            raise Exception(
                "Error {}: {}".format(response.status_code, response.text)
            )
        else:
            break

    data = response.json()

    while data.get("next"):
        url = data.get("next")
        while True:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 429:
                delay = int(response.headers.get("Retry-After"))
                time.sleep(delay)
            elif response.status_code != 200:  # if not success
                raise Exception(
                    "Error {}: {}".format(response.status_code, response.text)
                )
            else:
                break

        data["items"].extend(response.json()["items"])

    return data


def get_auth_token():
    """
    Function to get Spotify authentication token.

    Returns:
    str: Access token if successful, None otherwise
    """
    access_token = getattr(settings, "SPOTIFY_ACCESS_TOKEN", None)
    token_expiry_time = getattr(settings, "SPOTIFY_TOKEN_EXPIRY_TIME", None)

    if access_token and token_expiry_time > time.time():
        return access_token

    # Encode as Base64 for security
    message = "{}:{}".format(
        settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET
    )
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    headers = {
        "Authorization": "Basic {}".format(base64_message),
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
                    "Spotify API error {}: {}".format(
                        error_status, error_message
                    )
                )
            else:  # Authentication error object
                raise Exception(
                    "Spotify API error: {}, Description: {}".format(
                        response_data["error"], error_description
                    )
                )
    except (requests.RequestException, json.JSONDecodeError) as e:
        print("Error retrieving Spotify access token: {}".format(e))
        return None

    access_token = response_data.get("access_token")
    if not access_token:
        print("Error: Access token not present in Spotify response")
        return None
    token_expiry_time = time.time() + 3600 - 60  # 60 seconds safety margin

    setattr(settings, "SPOTIFY_ACCESS_TOKEN", access_token)
    setattr(settings, "SPOTIFY_TOKEN_EXPIRY_TIME", token_expiry_time)

    return access_token


artist_cache = {}


def get_artist_genres(artist_id):
    """
    Function to get the genres of a specific artist by ID.

    Parameters:
    artist_id (str): The Spotify ID of the artist

    Returns:
    list: List of genres if successful, empty list otherwise
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
                    "Spotify API error {}: {}".format(
                        error_status, error_message
                    )
                )
            else:  # Authentication error object
                raise Exception(
                    "Spotify API error: {}, Description: {}".format(
                        artist_data["error"], error_description
                    )
                )
    except requests.RequestException as e:
        print("Error retrieving genres for artist {}: {}".format(artist_id, e))
        return []

    # Extracting genres from the artist data
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
    album_ids (list): The list of Spotify IDs of the albums

    Returns:
    list: List of album details if successful, empty list otherwise
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
                        "Spotify API error {}: {}".format(
                            error_status, error_message
                        )
                    )
                else:  # Authentication error object
                    raise Exception(
                        "Spotify API error: {}, Description: {}".format(
                            album_data["error"], error_description
                        )
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
                    print("Genres TEST: ", artist["genres"])

            albums_data.append(album_data)
        except requests.RequestException as e:
            print(f"Failed to get album details for {album_id}. Error: {e}")
            continue

    return albums_data


def search_albums(query):
    """
    Function to search for albums on Spotify and retrieve their details.

    Parameters:
    query (str): The search query to find albums on Spotify.

    Returns:
    list: A list of album details if successful, an empty list otherwise.
    """

    access_token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    params = (
        ("q", query),
        ("type", "album"),
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
        print(album_data)  # Print the album data for debugging

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
                    "Spotify API error {}: {}".format(
                        error_status, error_message
                    )
                )
            else:  # Authentication error object
                raise Exception(
                    "Spotify API error: {}, Description: {}".format(
                        album_data["error"], error_description
                    )
                )

    except requests.RequestException as e:
        print(f"Error retrieving albums for query '{query}': {e}")
        return []

    return album_data


def get_album_ids(query):
    """
    Function to retrieve the Spotify IDs of albums based on a search query.

    Parameters:
    query (str): The search query to find albums on Spotify.

    Returns:
    list: A list of Spotify IDs of albums if successful,
    an empty list otherwise.
    """

    albums = search_albums(query)
    return [album["id"] for album in albums]
