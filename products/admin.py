from django.contrib import admin
from .models import Album, CD, Vinyl, TShirt


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
    list_display = ("album", "price", "on_sale", "get_quantity")
    list_filter = ("on_sale",)
    search_fields = ("album__album_id", "album__title")

    def get_quantity(self, obj):
        return obj.album.quantity

    get_quantity.short_description = "Quantity"


@admin.register(Vinyl)
class VinylAdmin(admin.ModelAdmin):
    list_display = ("album", "price", "on_sale", "get_quantity")
    list_filter = ("on_sale",)
    search_fields = ("album__album_id", "album__title")

    def get_quantity(self, obj):
        return obj.album.quantity

    get_quantity.short_description = "Quantity"


@admin.register(TShirt)
class TShirtAdmin(admin.ModelAdmin):
    list_display = ("album", "price", "on_sale", "get_quantity", "get_sizes")
    list_filter = ("on_sale",)
    search_fields = ("album__album_id", "album__title")

    def get_quantity(self, obj):
        return obj.album.quantity

    def get_sizes(self, obj):
        return ", ".join(obj.sizes.all().values_list("size", flat=True))

    get_quantity.short_description = "Quantity"
    get_sizes.short_description = "Sizes"
