from django.urls import path
from .views import view_cart, add_to_cart, empty_cart

app_name = "cart"

urlpatterns = [
    path("", view_cart, name="cart"),
    path("add/<item_id>/", add_to_cart, name="add_to_cart"),
    path("empty/", empty_cart, name="empty_cart"),
]
