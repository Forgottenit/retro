from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Album, Genre
from urllib.parse import urlencode
from django.db.models.functions import Lower
from django_user_agents.utils import get_user_agent


def album_model_view(request):
    """A view to show all albums, including search queries"""
    albums = Album.objects.annotate(artist_count=Count("artists")).order_by(
        "artists__artist_name"
    )

    search_query = request.GET.get("q")

    genres = Genre.objects.all()
    genre_query = request.GET.get("genre")
    sort = None
    direction = None

    sort_display_map = {
        "price_asc": "Price (low to high)",
        "price_desc": "Price (high to low)",
        "popularity_asc": "Rating (low to high)",
        "popularity_desc": "Rating (high to low)",
        "artists_asc": "Artist (A-Z)",
        "artists_desc": "Artist (Z-A)",
        "album_name_asc": "Album (A-Z)",
        "album_name_desc": "Album (Z-A)",
    }

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET.get("sort")
            sort = sortkey
            if sortkey == "album_name":
                sortkey = "lower_album_name"
                albums = albums.annotate(lower_album_name=Lower("album_name"))
            elif sortkey == "artists":
                sortkey = "lower_artists"
                albums = albums.annotate(
                    lower_artists=Lower("artists__artist_name")
                )

            if "direction" in request.GET:
                direction = request.GET.get("direction")
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            albums = albums.order_by(sortkey)

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
                | Q(genres__name__icontains=search_query)
            )

    if request.GET:
        if "sort" in request.GET or "q" in request.GET:
            page_number = 1
        else:
            page_number = request.GET.get("page")
    else:
        page_number = request.GET.get("page")

    # Convert QuerySet to list and remove duplicates
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

    # Set the number of albums per page based on screen size
    user_agent = get_user_agent(request)

    if user_agent.is_mobile:
        albums_per_page = 7  # 7 albums per page for mobile devices
    else:
        albums_per_page = 15  # 15 albums per page for larger screens

    paginator = Paginator(albums, albums_per_page)
    page_number = request.GET.get("page")
    albums = paginator.get_page(page_number)

    current_sorting = f"{sort}_{direction}"
    current_sorting_display = sort_display_map.get(current_sorting, "")

    context = {
        "albums": albums,
        "search_term": search_query,
        "genres": genres,
        "genre": genre_query,
        "params": params_str,
        "current_sorting": current_sorting,
        "current_sorting_display": current_sorting_display,
    }

    return render(
        request,
        "products/albums.html",
        context,
    )


def album_details(request, album_id):
    """A view to show one album and details"""
    album = get_object_or_404(Album, album_id=album_id)

    context = {
        "album": album,
    }

    return render(request, "products/album_details.html", context)
