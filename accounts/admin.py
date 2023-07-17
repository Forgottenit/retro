"""
Admin for User, Customer, Wishlist, Like, and Review.

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Wishlist, Like, Review, AlbumRequest


class WishlistInline(admin.TabularInline):
    """
    Inline for Wishlist model.
    """

    model = Wishlist
    extra = 1


class LikeInline(admin.TabularInline):
    """
    Inline for Like model.
    """

    model = Like
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    """
    Admin for Customer model
    """

    inlines = [WishlistInline, LikeInline]


class CustomerInline(admin.StackedInline):
    """
    Inline for Customer model.
    """

    model = Customer
    can_delete = False


class CustomUserAdmin(UserAdmin):
    """
    Custom Admin for User model
    """

    inlines = [CustomerInline]


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin for Review model,
    """

    list_display = ("customer", "album", "review_text", "created_date")


class AlbumRequestAdmin(admin.ModelAdmin):
    """
    Admin for AlbumRequest model,
    """

    list_display = (
        "request_title",
        "artist_name",
        "album_title",
        "message",
        "submitted_at",
    )


admin.site.register(AlbumRequest, AlbumRequestAdmin)

admin.site.register(Review, ReviewAdmin)

admin.site.unregister(User)
admin.site.register(
    Customer,
    CustomerAdmin,
)
admin.site.register(User, CustomUserAdmin)
