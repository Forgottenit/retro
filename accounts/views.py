from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer, Wishlist, Like, Review
from .forms import CustomerProfileForm, ReviewForm
from products.models import Album
from checkout.models import Order
from django.http import HttpResponseForbidden
from django.http import JsonResponse


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(Customer, user=request.user)

    if request.method == "POST":
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = CustomerProfileForm(instance=profile)
    orders = profile.orders.all()

    # Get the wishlist albums
    try:
        wishlists = profile.wishlists.all()
    except KeyError:
        wishlists = None

    template = "accounts/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "wishlists": wishlists,  # Pass the wishlist to the template
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def like_album(request, album_id):
    album = get_object_or_404(Album, album_id=album_id)
    like, created = Like.objects.get_or_create(
        user=request.user.customer, album=album
    )

    # if it was already liked, unlike it
    if not created:
        if like.liked:
            like.delete()
            album.popularity = max(0, album.popularity - 1)
        else:
            like.liked = True
            like.save()
            album.popularity += 1
    else:
        like.liked = True
        like.save()
        album.popularity += 1

    album.save()

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def add_to_wishlist(request, album_id):
    """Add an item to the wishlist"""
    album = get_object_or_404(Album, album_id=album_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        customer=request.user.customer, album=album
    )

    if created:
        messages.success(request, f"Added {album.album_name} to your wishlist")
    else:
        messages.info(
            request, f"{album.album_name} is already in your wishlist"
        )

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_from_wishlist(request, album_id):
    """Remove an item from the wishlist"""
    album = get_object_or_404(Album, album_id=album_id)
    wishlist_item = get_object_or_404(
        Wishlist, customer=request.user.customer, album=album
    )

    if wishlist_item:
        wishlist_item.delete()
        messages.success(
            request, f"Removed {album.album_name} from your wishlist"
        )
    else:
        messages.info(request, f"{album.album_name} is not in your wishlist")

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)


# @login_required
def add_review(request, album_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    album = get_object_or_404(Album, album_id=album_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.album = album
            review.customer = request.user.customer
            review.save()

            return redirect("products:album_details", album_id=album.album_id)
    else:
        form = ReviewForm()

    context = {"form": form, "album": album}
    return render(request, "accounts/add_review.html", context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.user != review.customer.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect(
                "products:album_details", album_id=review.album.album_id
            )
    else:
        form = ReviewForm(instance=review)

    context = {"form": form, "album": review.album}
    return render(request, "accounts/edit_review.html", context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.customer.user:
        return HttpResponseForbidden()
    album_id = review.album.album_id
    review.delete()
    return redirect("products:album_details", album_id=album_id)
