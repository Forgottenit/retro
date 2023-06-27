from django.shortcuts import render
from .models import Album
from django.core.paginator import Paginator


def album_model_view(request):
    print("TEST")
    albums = Album.objects.all().order_by(
        "artists__name"
    )  # Fetch album instances
    paginator = Paginator(albums, 21)
    page_number = request.GET.get("page")
    albums = paginator.get_page(page_number)
    return render(
        request, "products/albums.html", {"albums": albums}
    )  # Pass albums to template
