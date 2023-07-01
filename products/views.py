from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Album


def album_model_view(request):
    """A view to show all albums, including search queries"""

    albums = Album.objects.all().order_by("artists__artist_name")
    search_query = request.GET.get("q")

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

    paginator = Paginator(albums, 21)
    page_number = request.GET.get("page")
    albums = paginator.get_page(page_number)

    return render(
        request,
        "products/albums.html",
        {"albums": albums, "search_term": search_query},
    )
