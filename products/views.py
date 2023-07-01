from django.shortcuts import render
from .models import Album, Artist
from django.core.paginator import Paginator
from django.db.models import Q


def album_model_view(request):
    search_query = request.GET.get("q")
    print("TEST")
    albums = Album.objects.all().order_by("artists__artist_name")
    artists = Artist.objects.all().order_by("artist_name")

    if search_query:
        albums = albums.filter(
            Q(album_name__icontains=search_query)
            | Q(artists__artist_name__icontains=search_query)
        )

    paginator = Paginator(albums, 21)
    page_number = request.GET.get("page")
    albums = paginator.get_page(page_number)
    return render(
        request,
        "products/albums.html",
        {"albums": albums, "artists": artists, "query": search_query},
    )
