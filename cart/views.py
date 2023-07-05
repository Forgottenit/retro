from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """Returns Cart page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a quantity to cart"""

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session["cart"] = cart

    return redirect(redirect_url)


def empty_cart(request):
    """Method to empty Cart when needed TO BE REMOVED"""
    request.session[
        "cart"
    ] = {}  # Set the cart dictionary to an empty dictionary
    return redirect("cart:view_cart")


def edit_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    try:
        quantity = int(request.POST.get("quantity"))
    except ValueError:
        return HttpResponse(
            status=400
        )  # Return 400 Bad Request error for invalid data

    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id, None)

    request.session["cart"] = cart
    return redirect(reverse("cart:view_cart"))


def delete_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        cart = request.session.get("cart", {})
        cart.pop(item_id)
        print("CART 1:", cart)
        request.session["cart"] = cart
        print("CART 2:", cart)
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(
            status=500
        )  # Return 500 Server Error for unexpected issues
