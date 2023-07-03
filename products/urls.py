from django.urls import path
from .views import album_model_view, album_details

app_name = "products"

urlpatterns = [
    path("album/", album_model_view, name="albums"),
    path("<str:album_id>", album_details, name="album_details"),
]
