"""
Module for Accounts with views for login, likes, wishlist, 
order history, and Album requests 
"""

import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

from products.models import Album
from checkout.models import Order
from .models import Customer, Wishlist, Like, Review, AlbumRequest
from .forms import CustomerProfileForm, ReviewForm, AlbumRequestForm


@login_required
def profile(request):
    """
    Function to display and manage the user's profile page.

    Parameters:
    - request: HTTP request

    Returns:
    - Rendered template of the user profile page.
    """
    profile = get_object_or_404(Customer, user=request.user)
    album_requests = AlbumRequest.objects.filter(customer=profile)

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "profile_form":
            form = CustomerProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("accounts:profile")
        elif form_type == "album_request_form":
            form = AlbumRequestForm(request.POST)
            if form.is_valid():
                new_request = form.save(commit=False)
                new_request.customer = profile
                new_request.save()
                messages.success(
                    request, "Album Request updated successfully"
                )
                return redirect("accounts:profile")

        messages.error(
            request, "There was an error with the form. Please try again."
        )
        return redirect("accounts:profile")

    elif request.method == "GET":
        profile_form = CustomerProfileForm(instance=profile)
        album_request_form = AlbumRequestForm()

        orders = profile.orders.all()

        # get wishlist albums
        try:
            wishlists = profile.wishlists.all()
        except KeyError:
            wishlists = None

        template = "accounts/profile.html"
        context = {
            "profile_form": profile_form,
            "album_request_form": album_request_form,
            "orders": orders,
            "wishlists": wishlists,
            "on_profile_page": True,
            "album_requests": album_requests,
        }

        return render(request, template, context)


@login_required
def like_album(request, album_id):
    """
    Function to manage liking of an album by a user.

    Parameters:
    - request: HTTP request
    - album_id: ID of the album to be liked

    Returns:
    - Redirect to the previous page.
    """
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
    """
    Function to add an album to the user's wishlist.

    Parameters:
    - request: HTTP request
    - album_id: ID of the album to be added to the wishlist

    Returns:
    - Redirect to the previous page.
    """

    album = get_object_or_404(Album, album_id=album_id)
    if request.user.is_authenticated and request.user.is_active:
        wishlist_item, created = Wishlist.objects.get_or_create(
            customer=request.user.customer, album=album
        )

        if created:
            messages.success(
                request, f"Added {album.album_name} to your wishlist"
            )
        else:
            messages.info(
                request, f"{album.album_name} is already in your wishlist"
            )

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_from_wishlist(request, album_id):
    """
    Function to remove an album from the user's wishlist.

    Parameters:
    - request: HTTP request
    - album_id: ID of the album to be removed from the wishlist

    Returns:
    - Redirect to the previous page.
    """
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
    """
    Function to display a user's past order information.

    Parameters:
    - request: HTTP request
    - order_number: Order number of old orders

    Returns:
    - Rendered template of checkout success page
    """
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


@login_required
def add_review(request, album_id):
    """
    Function to add a review for an album.

    Parameters:
    - request: HTTP request
    - album_id: ID of the album to be reviewed

    Returns:
    - If POST: Redirect to album details page after review is saved.
    - Else: Render the template of the add review page.
    """
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

            return redirect(
                "products:album_details", album_id=album.album_id
            )
    else:
        form = ReviewForm()

    context = {"form": form, "album": album}
    return render(request, "accounts/add_review.html", context)


@login_required
def edit_review(request, review_id):
    """
    Function to edit an existing review.
    User must be the author of the review.

    Parameters:
    - request: HTTP request
    - review_id: ID of the review to be edited

    Returns:
    - If POST: Redirect to album details page after review is updated.
    - Else: Render the template of edit review page.
    """
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
    """
    Function to delete an existing review.
    User must be the author of the review.

    Parameters:
    - request: HTTP request
    - review_id: ID of the review to be deleted

    Returns:
    - Redirect to album details page after review deleted.
    """
    review = get_object_or_404(Review, pk=review_id)
    if (
        not request.user.is_superuser
        and request.user != review.customer.user
    ):
        return HttpResponseForbidden()
    album_id = review.album.album_id
    review.delete()
    return redirect("products:album_details", album_id=album_id)


@login_required
def request_album(request):
    """
    A view for authenticated users to request an album.

    If the method is POST, the submitted form is validated, and if valid, a new
    AlbumRequest is created and the user is redirected to their profile page.

    If the method is not POST, a new form is rendered on the profile.html page.
    """
    if request.method == "POST":
        form = AlbumRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.customer = request.user.customer
            new_request.save()
            return redirect("accounts:profile")
    else:
        form = AlbumRequestForm(instance=request.user.customer)
    return render(request, "profile.html", {"form": form})


@login_required
def edit_album_request(request, id):
    """
    A view for authenticated users to edit a previously made album request.

    If the method is POST, the submitted form is validated and if valid,
    the changes are saved, and the user is redirected to their profile page.

    If the method is not POST, an edit form is rendered on the
    accounts/edit_request.html page.
    """
    album_request = get_object_or_404(AlbumRequest, id=id)
    if request.method == "POST":
        form = AlbumRequestForm(request.POST, instance=album_request)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
    else:
        form = AlbumRequestForm(instance=album_request)
    return render(
        request, "accounts/edit_request.html", {"album_request_form": form}
    )


@login_required
def delete_album_request(request, id):
    """
    A view for authenticated users to delete a previously made album request.

    If the user who made the request is not the current user,
    an HTTP 403 Forbidden response is returned.

    If the method is POST, the AlbumRequest is deleted,
    a success message is added, and the user is redirected to
    their profile page.

    If the method is not POST, a delete confirmation page is rendered.
    """
    album_request = get_object_or_404(AlbumRequest, id=id)

    # Check if the current user is the one who made the request
    if album_request.customer.user != request.user:
        return HttpResponseForbidden()

    # If the method is POST, then delete the object
    if request.method == "POST":
        album_request.delete()
        messages.success(request, "Album Request deleted successfully")
        return redirect("accounts:profile")

    return render(
        request, "delete_confirm.html", {"album_request": album_request}
    )
