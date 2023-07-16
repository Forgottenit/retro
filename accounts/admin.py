"""
This module defines the Django admin interface for the User and Customer models
and related inline models - Wishlist, Like, and Review.

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Wishlist, Like, Review


class WishlistInline(admin.TabularInline):
    """
    Defines an inline admin interface for Wishlist model.
    """

    model = Wishlist
    extra = 1


class LikeInline(admin.TabularInline):
    """
    Defines an inline admin interface for Like model.
    """

    model = Like
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Customer model,
    including inline interfaces for Wishlist and Like models.
    """

    inlines = [WishlistInline, LikeInline]


class CustomerInline(admin.StackedInline):
    """
    Defines an inline admin interface for Customer model.
    """

    model = Customer
    can_delete = False


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for User model,
    including inline interface for Customer model.
    """

    inlines = [CustomerInline]


class ReviewAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Review model,
    specifying some fields to display.
    """

    list_display = ("customer", "album", "review_text", "created_date")


admin.site.register(Review, ReviewAdmin)

admin.site.unregister(User)
admin.site.register(
    Customer,
    CustomerAdmin,
)
admin.site.register(User, CustomUserAdmin)
