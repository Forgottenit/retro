from django.urls import path
from .views import album_model_view

app_name = "products"

urlpatterns = [
    path("album/", album_model_view, name="albums"),
]
