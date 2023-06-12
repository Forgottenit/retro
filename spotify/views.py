from django.shortcuts import render
import json

def album_view(request):
    # Load data from the JSON file
    with open('album_fixtures.json', 'r') as file:
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
    return render(request, 'spotify/album.html', context)
