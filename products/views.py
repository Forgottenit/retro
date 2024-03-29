"""
Module for product app views, load albums, album_model_view,
album_details, add_product, edit product, delete product,
delete Artist
"""
from urllib.parse import urlencode
from django.http import HttpResponseRedirect
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
)
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django_user_agents.utils import get_user_agent
from accounts.models import Like
from product_data.load_models import load_models
from .models import Album, Genre, Artist
from .forms import LoadAlbumsForm, ProductForm


@login_required
def load_albums(request, search_field="artist"):
    """
    View function to load albums from Spotify and store them in the database.
    Only accessible to superusers.

    Returns:
    - If the request method is GET:
        - Render template with the form to load albums.
    - If the request method is POST and the form is valid:
        - Redirect to the albums view with a success message.
    - If the request method is POST and the form is invalid:
        - Redirect to the albums view with an error message.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = LoadAlbumsForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            search_field = form.cleaned_data["search_field"]
            load_models(query, search_field)
            messages.success(request, "Albums loaded successfully!")
            return redirect("products:albums")
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = LoadAlbumsForm()

    albums = Album.objects.all().order_by("artists__artist_name")

    return render(
        request,
        "products/add_product.html",
        {"albums": albums, "form": form},
    )


def album_model_view(request):
    """
    View function to display all albums with search and sorting functionality.

    Returns:
    - Rendered template with the albums, search queries, and sorting options.
    """
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
                albums = albums.annotate(
                    lower_album_name=Lower("album_name")
                )
            elif sortkey == "artists":
                sortkey = "lower_main_artist_name"
                albums = albums.annotate(
                    lower_main_artist_name=Lower("main_artist__artist_name")
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
            return HttpResponseRedirect(
                request.META.get("HTTP_REFERER", "/")
            )
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

    # Convert QuerySet to list and remove duplicates
    albums = list(albums)
    seen = set()
    unique_albums = []
    for album in albums:
        if album.album_id not in seen:
            unique_albums.append(album)
            seen.add(album.album_id)
    albums = unique_albums

    params = (
        request.GET.copy()
    )  # make a mutable copy of request.GET QueryDict
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

    if request.user.is_authenticated:
        is_customer = hasattr(request.user, "customer")
        if is_customer:
            likes = Like.objects.filter(
                user=request.user.customer, liked=True
            )
            liked_albums = [like.album.album_id for like in likes]
        else:
            likes = None
            liked_albums = None
    else:
        is_customer = False
        likes = None
        liked_albums = None

    context = {
        "albums": albums,
        "search_term": search_query,
        "genres": genres,
        "genre": genre_query,
        "params": params_str,
        "current_sorting": current_sorting,
        "current_sorting_display": current_sorting_display,
        "liked_albums": liked_albums,
        "is_customer": is_customer,
    }

    return render(
        request,
        "products/albums.html",
        context,
    )


def album_details(request, album_id):
    """
    View function to display the details of a specific album.

    Parameters:
    - album_id (str): The ID of the album.

    Returns:
    - Rendered template with the album details.
    """
    album = get_object_or_404(Album, album_id=album_id)

    context = {
        "album": album,
    }

    return render(request, "products/album_details.html", context)


@login_required
def add_product(request):
    """
    View function to add a product to the store.

    Only accessible to superusers.

    Returns:
    - If the request method is GET:
        - Rendered template with the product form.
    - If the request method is POST and the form is valid:
        - Redirect to the album details page of the added product,
           with a success message.
    - If the request method is POST and the form is invalid:
        - Rendered template with the product form and an error message.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(
                reverse("products:album_details", args=[album.album_id])
            )
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, album_id):
    """
    View function to edit a product in the store.

    Only accessible to superusers.

    Parameters:
    - album_id (str): The ID of the album to edit.

    Returns:
    - If the request method is GET:
        - Rendered template with the product form filled with existing data.
    - If the request method is POST and the form is valid:
        - Redirect to the album details page of the edited product,
           with a success message.
    - If the request method is POST and the form is invalid:
        - Rendered template with the product form and an error message.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    album = get_object_or_404(Album, album_id=album_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(
                reverse("products:album_details", args=[album.album_id])
            )
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=album)
        messages.info(request, f"You are editing {album.album_name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "album": album,
    }

    return render(request, template, context)


@login_required
def delete_product(request, album_id):
    """
    View function to delete a product from the store.

    Only accessible to superusers.

    Parameters:
    - album_id (str): The ID of the album to delete.

    Returns:
    - Redirect to the albums view with a success message.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    album = get_object_or_404(Album, album_id=album_id)
    album.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products:albums"))


@login_required
def delete_artist(request, artist_id):
    """
    View function to delete an artist and all related objects from the store.

    Only accessible to superusers.

    Parameters:
    - artist_id (str): The ID of the artist to delete.

    Returns:
    - Redirect to the albums view with a success message.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    try:
        artist = Artist.objects.get(artist_id=artist_id)
        artist.delete()
        messages.success(request, "Artist and related objects deleted!")
    except ObjectDoesNotExist:
        messages.error(
            request, "The artist you are trying to delete does not exist."
        )
        return redirect(reverse("products:albums"))

    return redirect(reverse("products:albums"))
