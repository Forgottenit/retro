"""
Module to set App configuration for Home app
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Set default field for Home App
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "home"
