from django.contrib import admin
from django.urls import path
from .views import album_view
from . import views

app_name = 'spotify'

urlpatterns = [
    path('album/', views.album_view, name='album'),
]
