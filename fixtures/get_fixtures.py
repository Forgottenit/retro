import requests
import base64
from django.conf import settings
import json


def get_auth_token():
    # Encode as Base64
    message = f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    headers = {
        'Authorization': f'Basic {base64_message}',
    }

    data = {
        'grant_type': 'client_credentials',
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

    return response.json()["access_token"]


def get_album_details(album_ids):
    access_token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    albums_data = []

    for album_id in album_ids:
        response = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=headers)
        albums_data.append(response.json())

    return albums_data


def search_albums(query):
    access_token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    params = (
        ('q', query),
        ('type', 'album'),
    )

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    album_data = response.json()["albums"]["items"]
    print(album_data)  # Print the album data for debugging

    return response.json()["albums"]["items"]


def get_album_ids(query):
    albums = search_albums(query)
    return [album["id"] for album in albums]


def create_fixtures(artist_name):
    album_ids = get_album_ids(artist_name)
    print("Album IDs:", album_ids)
    album_data = get_album_details(album_ids)
    print("Album Data:", album_data)
    try:
        with open("fixtures/album_fixtures.json", "r", encoding='utf-8') as f:
            fixtures = json.load(f)
    except FileNotFoundError:
        fixtures = []
    # Extract all existing album IDs in the fixtures
    existing_album_ids = {fixture['fields']['id'] for fixture in fixtures}

    start_pk = len(fixtures)

    for i, album in enumerate(album_data, start=start_pk):
        # Skip if this album is already in the fixtures
        if album['id'] in existing_album_ids:
            continue

        fixture = {
            "model": "myapp.album",  # Replace with your actual model
            "pk": i,
            "fields": album,
        }
        fixtures.append(fixture)

    with open("fixtures/album_fixtures.json", "w", encoding='utf-8') as f:
        json.dump(fixtures, f)
