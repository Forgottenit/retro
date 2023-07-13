from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer, Wishlist, Like
from .forms import CustomerProfileForm
from products.models import Album
from checkout.models import Order
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
        like.liked = not like.liked
    else:
        like.liked = True

    like.save()

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def add_to_wishlist(request, item_id):
    """Add an item to the wishlist"""
    album = get_object_or_404(Album, album_id=item_id)
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
