from django.contrib import admin
from .models import Customer, Wishlist


class WishlistInline(admin.TabularInline):
    model = Wishlist
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    inlines = [WishlistInline]


admin.site.register(Customer, CustomerAdmin)
