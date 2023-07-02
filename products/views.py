from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Album, Genre
from urllib.parse import urlencode


def album_model_view(request):
    """A view to show all albums, including search queries"""
    albums = Album.objects.annotate(artist_count=Count("artists")).order_by(
        "artists__artist_name"
    )

    search_query = request.GET.get("q")

    genres = Genre.objects.all()
    genre_query = request.GET.get("genre")
    print(genre_query)

    if genre_query is not None and genre_query != "All":
        albums = albums.filter(genres__name__icontains=genre_query)
    elif genre_query == "All":
        albums = albums.all()

    if search_query is not None:
        search_query = search_query.strip()
        if not search_query:
            messages.error(request, "You didn't enter any search criteria!")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
        else:
            albums = albums.filter(
                Q(album_name__icontains=search_query)
                | Q(artists__artist_name__icontains=search_query)
            )

    # Convert QuerySet to list and remove duplicates at Python level
    albums = list(albums)
    seen = set()
    albums = [
        x
        for x in albums
        if x.album_id not in seen and not seen.add(x.album_id)
    ]

    params = request.GET.copy()  # make a mutable copy of request.GET QueryDict
    page_number = params.pop("page", None)  # remove 'page' if it exists
    params_str = (
        params.urlencode()
    )  # convert the QueryDict to a URL-encoded string

    paginator = Paginator(albums, 18)
    page_number = request.GET.get("page")
    albums = paginator.get_page(page_number)

    return render(
        request,
        "products/albums.html",
        {
            "albums": albums,
            "search_term": search_query,
            "genres": genres,
            "genre": genre_query,
            "params": params_str,
        },
    )
