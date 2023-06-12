from django.urls import path
from .views import update_albums  

urlpatterns = [

    path('update-albums/', update_albums, name='update-albums'),
]
