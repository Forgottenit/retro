"""
Contexts module to pass Cart Contents
"""

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Album


def cart_contents(request):
    """
    Function to store and calculate total of Cart
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})

    for item_id, quantity in cart.items():
        album = get_object_or_404(Album, album_id=item_id)
        total += quantity * album.price
        product_count += quantity
        cart_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "album": album,
                "artists": album.artists.all(),
                "copyrights": album.copyrights,
            }
        )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100
        )
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
