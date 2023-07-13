from django.contrib import admin
from .models import Customer, Wishlist, Like


class WishlistInline(admin.TabularInline):
    model = Wishlist
    extra = 1


class LikeInline(admin.TabularInline):
    model = Like
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    inlines = [WishlistInline, LikeInline]


admin.site.register(Customer, CustomerAdmin)
