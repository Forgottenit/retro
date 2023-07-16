"""
Checkout App Configuration
"""

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Class setting signals for Checkout
    """

    name = "checkout"

    def ready(self):
        import checkout.signals
