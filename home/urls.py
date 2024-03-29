"""
Module to Set URLS for Home app
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("privacy/", views.privacy_policy, name="privacy_policy"),
]
