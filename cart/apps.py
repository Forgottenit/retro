"""
App configuration for Cart App
"""

from django.apps import AppConfig


class CartConfig(AppConfig):
    """
    Sets default auto field for Cart app
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "cart"
