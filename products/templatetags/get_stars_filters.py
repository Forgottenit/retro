"""
Module for products filters/ template tags
"""
from django import template

register = template.Library()


@register.filter
def get_stars(rating):
    """
    Filter to calculate and return half-full
    total for stars - non-int = half full
    """
    full_stars = int(rating)
    is_half_star = rating % 1 != 0
    return {"full_stars": range(full_stars), "is_half_star": is_half_star}


@register.filter
def times(number):
    """
    Filter to return range of int
    """
    return range(number)
