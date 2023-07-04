from django.shortcuts import render


def view_cart(request):
    """Returns Cart page"""

    return render(request, "cart/cart.html")
