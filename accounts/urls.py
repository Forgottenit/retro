from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_history/<order_number>",
        views.order_history,
        name="order_history",
    ),
    path("like_album/<str:album_id>/", views.like_album, name="like_album"),
    path("add/<str:album_id>/", views.add_to_wishlist, name="add_to_wishlist"),
]
