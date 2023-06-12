from django.contrib import admin
from django.urls import path
from .views import album_view, update_albums

from . import views

app_name = 'spotify'

urlpatterns = [
    path('album/', views.album_view, name='album'),
    path('update_albums/', views.update_albums, name='update-albums'),  # add this line
]
