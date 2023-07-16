"""
Filter to Calc total price
"""

from django import template


register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """
    Returns Price multiplied by quantity
    """
    return price * quantity
