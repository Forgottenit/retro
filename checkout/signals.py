from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_order_on_lineitem_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    if created or instance.quantity_changed:
        instance.order.update_total(
            update_fields=["order_total", "grand_total"]
        )


@receiver(post_delete, sender=OrderLineItem)
def update_order_on_lineitem_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total(update_fields=["order_total", "grand_total"])
