from django.shortcuts import render
import json
from django.http import HttpResponseRedirect
from fixtures.get_fixtures import create_fixtures
from django.urls import reverse


def album_view(request):
    # Load data from the JSON file
    with open('fixtures/filtered_albums/filtered_album_fixtures.json', 'r') as file:
        data = json.load(file)

    # Create a list of albums, each of which is a dictionary containing 
    # the album data, artists, and tracks
    albums = []
    for album in data:
        album_fields = album['fields']
        album_artists = album_fields['artists']
        album_tracks = album_fields['tracks']['items']

        album_info = {
            'album_data': album_fields,
            'album_artists': album_artists,
            'album_tracks': album_tracks
        }

        albums.append(album_info)

    # Pass the data to the template
    context = {
        'albums': albums
    }

    # Render the template with the data
    return render(request, 'fixtures/album.html', context)

def update_albums(request):
    print("Request method:", request.method)  # This is for debugging.
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        print("Artist name:", artist_name)  # This is for debugging.
        create_fixtures(artist_name)
    return HttpResponseRedirect(reverse('fixtures:album'))  # Redirect to the album page
