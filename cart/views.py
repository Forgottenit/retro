from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from django.contrib import messages
from products.models import Album


def view_cart(request):
    """Returns Cart page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a quantity to cart"""
    product = get_object_or_404(Album, album_id=item_id)

    quantity_str = request.POST.get("quantity")
    if quantity_str:
        quantity = int(request.POST.get("quantity"))
    else:
        quantity = 1

    # if not quantity_str:
    #     messages.error(request, "Quantity cannot be empty.")
    #     return redirect(request.META.get("HTTP_REFERER", "/"))

    # quantity = int(request.POST.get("quantity"))

    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            f"Updated {product.album_name} quantity to {cart[item_id]}",
        )
    else:
        cart[item_id] = quantity
        messages.success(request, f"Added {product.album_name} to your cart")

    request.session["cart"] = cart

    redirect_url = request.POST.get("redirect_url")
    if not redirect_url:
        return redirect(request.path)  # If redirect_url is None or empty
        # redirect_url = "cart:view_cart"

    return redirect(redirect_url)


def edit_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Album, album_id=item_id)

    quantity_str = request.POST.get("quantity")
    if not quantity_str:
        messages.error(request, "Quantity cannot be empty.")
        return redirect(request.META.get("HTTP_REFERER", "/"))

    try:
        quantity = int(request.POST.get("quantity"))
    except ValueError:
        messages.error(
            request, "Invalid quantity. Please enter a valid number."
        )
        return redirect(request.META.get("HTTP_REFERER", "/"))

    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request,
            f"Updated {product.album_name} quantity to {cart[item_id]}",
        )
    else:
        cart.pop(item_id, None)
        messages.success(
            request, f"Removed {product.album_name} from your cart"
        )

    request.session["cart"] = cart
    return redirect(reverse("cart:view_cart"))


def delete_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    product = get_object_or_404(Album, album_id=item_id)

    try:
        cart = request.session.get("cart", {})
        cart.pop(item_id)
        messages.success(
            request, f"Removed {product.album_name} from your cart"
        )

        request.session["cart"] = cart

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(
            status=500
        )  # Return 500 Server Error for unexpected issues
