from django.shortcuts import render
from django.shortcuts import render
import json


def album_view(request):
    # Load data from the JSON file
    with open('album_fixtures.json', 'r') as file:
        data = json.load(file)

    # Extract the relevant fields from the data
    album_data = data[0]['fields']
    album_artists = album_data['artists']
    album_tracks = album_data['tracks']['items']

    # Pass the data to the template
    context = {
        'album_data': album_data,
        'album_artists': album_artists,
        'album_tracks': album_tracks
    }

    # Render the template with the data
    return render(request, 'spotify/album.html', context)
