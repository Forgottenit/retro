from django.urls import path
from . import views

app_name = "product_data"

urlpatterns = [
    path("load_albums/", views.load_albums, name="load_albums"),
]
