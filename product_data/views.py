from django.shortcuts import render
from .load_models import load_models
from products.models import Album
from django.core.paginator import Paginator


def load_albums(request):
    if request.method == "POST":
        artist_name = request.POST.get("artist_name")
        load_models(artist_name)

    albums = Album.objects.all().order_by("artists__artist_name")
    paginator = Paginator(albums, 21)
    page_number = request.GET.get("page")
    albums = paginator.get_page(page_number)

    return render(request, "products/albums.html", {"albums": albums})
