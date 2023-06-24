from django.contrib import admin
from django.urls import path
from . import views

from . import views

app_name = "fixtures"

urlpatterns = [
    path("album/", views.album_view, name="album"),
    path("update_albums/", views.update_albums, name="update_albums"),
    path("load_albums/", views.load_albums, name="load_albums"),
]
