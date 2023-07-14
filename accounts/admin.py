from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer, Wishlist, Like, Review


class WishlistInline(admin.TabularInline):
    model = Wishlist
    extra = 1


class LikeInline(admin.TabularInline):
    model = Like
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    inlines = [WishlistInline, LikeInline]


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [CustomerInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("customer", "album", "review_text", "created_date")


admin.site.register(Review, ReviewAdmin)

admin.site.unregister(User)
admin.site.register(
    Customer,
    CustomerAdmin,
)
admin.site.register(User, CustomUserAdmin)
