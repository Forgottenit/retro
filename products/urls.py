from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    # path("add/", views.add_product, name="add_product"),
    path("album/", views.album_model_view, name="albums"),
    path("load_albums/", views.load_albums, name="load_albums"),
    path("edit/<str:album_id>/", views.edit_product, name="edit_product"),
    path(
        "delete/<str:album_id>/", views.delete_product, name="delete_product"
    ),
    path(
        "delete_artist/<str:artist_id>/",
        views.delete_artist,
        name="delete_artist",
    ),
    path("album/<str:album_id>/", views.album_details, name="album_details"),
]
