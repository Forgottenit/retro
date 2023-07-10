from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("album/", views.album_model_view, name="albums"),
    path("<str:album_id>/", views.album_details, name="album_details"),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
