"""
Module for product_data app configuration
"""

from django.apps import AppConfig


class ProductDataConfig(AppConfig):
    """
    Class setting product_data app default fields
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "product_data"
