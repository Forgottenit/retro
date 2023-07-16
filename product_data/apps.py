"""
Module for product data app configuration
"""

from django.apps import AppConfig


class ProductDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "product_data"
