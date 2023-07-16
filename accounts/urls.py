"""
URLS For accounts app
"""
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
    path(
        "add/<str:album_id>/", views.add_to_wishlist, name="add_to_wishlist"
    ),
    path(
        "remove/<str:album_id>/",
        views.remove_from_wishlist,
        name="remove_from_wishlist",
    ),
    path(
        "album/<str:album_id>/add_review/",
        views.add_review,
        name="add_review",
    ),
    path(
        "review/<int:review_id>/edit/", views.edit_review, name="edit_review"
    ),
    path(
        "review/<int:review_id>/delete/",
        views.delete_review,
        name="delete_review",
    ),
    path("request-album/", views.request_album, name="request-album"),
    path(
        "edit-request/<int:id>/edit",
        views.edit_album_request,
        name="edit-request",
    ),
    path(
        "delete-request/<int:id>/delete",
        views.delete_album_request,
        name="delete-request",
    ),
]
