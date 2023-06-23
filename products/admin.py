from django.contrib import admin
from .models import Album, CD, Vinyl, TShirt, TShirtVariant
from django.utils.safestring import mark_safe


class ImageDisplayMixin:
    def get_image(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.image.url,
                    width=50,
                    height=50,
                )
            )
        else:
            return "No Image"

    get_image.short_description = "Image"


@admin.register(Album)
class AlbumAdmin(ImageDisplayMixin, admin.ModelAdmin):
    list_display = (
        "album_id",
        "release_date",
        "total_tracks",
        "popularity",
        "album_type",
        "label",
        "copyright",
        "explicit",
        "get_image",
    )
    search_fields = ("album_id", "label")


@admin.register(CD)
class CDAdmin(ImageDisplayMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "album",
        "quantity",
        "price",
        "on_sale",
        "get_image",
    )
    search_fields = ("name", "album__name")
    list_filter = ("on_sale",)


@admin.register(Vinyl)
class VinylAdmin(ImageDisplayMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "album",
        "quantity",
        "price",
        "on_sale",
        "get_image",
    )
    search_fields = ("name", "album__name")
    list_filter = ("on_sale",)


@admin.register(TShirt)
class TShirtAdmin(ImageDisplayMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "album",
        "sleeve_length",
        "colour",
        "on_sale",
        "get_image",
    )
    search_fields = ("name", "description", "album__album_id")
    list_filter = ("on_sale", "sleeve_length", "colour")


@admin.register(TShirtVariant)
class TShirtVariantAdmin(ImageDisplayMixin, admin.ModelAdmin):
    list_display = (
        "tshirt",
        "size",
        "quantity",
        "get_image",
    )
    search_fields = (
        "tshirt__name",
        "tshirt__album__album_id",
        "size__size",
    )
