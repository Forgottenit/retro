import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from fixtures.get_fixtures import create_fixtures



def format_duration(duration_ms):
    minutes = duration_ms // 60000
    seconds = (duration_ms // 1000) % 60

    if minutes == 0:
        return f"{seconds} secs"
    else:
        return f"{minutes}:{seconds:02d} mins"


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

        # Process album fields
        album_info = {
            'album_data': album_fields,
            'album_artists': album_artists,
            'album_tracks': album_tracks,
        }

        # Process track details
        for track in album_tracks:
            track['duration_formatted'] = format_duration(track['duration_ms'])

        albums.append(album_info)

    # Pass the data to the template
    context = {
        'albums': albums
    }

    # Render the template with the data
    return render(request, 'fixtures/album.html', context)


def update_albums(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        create_fixtures(artist_name)
    return HttpResponseRedirect(reverse('fixtures:album'))  # Redirect to the album page
