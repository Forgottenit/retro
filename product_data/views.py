# from django.shortcuts import render

# from .load_models import load_models
# from products.models import Album
# from django.core.paginator import Paginator

# from .forms import LoadAlbumsForm


# def load_albums(request):
#     form = LoadAlbumsForm(request.POST or None)
#     if form.is_valid():
#         query = form.cleaned_data["query"]
#         search_field = form.cleaned_data["search_field"]
#         load_models(query, search_field)

#     albums = Album.objects.all().order_by("artists__artist_name")
#     paginator = Paginator(albums, 21)
#     page_number = request.GET.get("page")
#     albums = paginator.get_page(page_number)

#     return render(request, "products/albums.html", {"albums": albums})
