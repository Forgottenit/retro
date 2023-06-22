import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from fixtures.get_fixtures import create_fixtures
from json.decoder import JSONDecodeError


def album_view(request):
    albums = []

    # Load data from the JSON file
    try:
        with open(
            "fixtures/album_fixtures.json", "r", encoding="utf-8"
        ) as file:
            data = json.load(file)

        # Check if the data is empty or not
        if data:
            for album in data:
                album_fields = album["fields"]
                album_artists = album_fields["artists"]
                album_tracks = album_fields["tracks"]["items"]
                album_images = album_fields.get("album_images", [])

                album_info = {
                    "album_data": album_fields,
                    "album_artists": album_artists,
                    "album_tracks": album_tracks,
                    "album_images": album_images,
                }

                albums.append(album_info)
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle the case when the JSON file is not found or empty
        pass

    context = {"albums": albums}
    return render(request, "fixtures/album.html", context)


def update_albums(request):
    if request.method == "POST":
        artist_name = request.POST.get("artist_name")
        try:
            create_fixtures(artist_name)
        except JSONDecodeError as e:
            print("Error occurred while decoding JSON response:", str(e))
    return HttpResponseRedirect(reverse("fixtures:album"))
