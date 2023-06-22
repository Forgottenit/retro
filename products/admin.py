from django.contrib import admin
from .models import Album, CD, Vinyl, TShirt, TShirtVariant
from django.utils.safestring import mark_safe


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
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


@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
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


@admin.register(Vinyl)
class VinylAdmin(admin.ModelAdmin):
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


@admin.register(TShirt)
class TShirtAdmin(admin.ModelAdmin):
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


@admin.register(TShirtVariant)
class TShirtVariantAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "get_album",
        "size",
        "quantity",
        "get_image",
    )
    search_fields = (
        "tshirt__name",
        "tshirt__album__album_id",
        "size__size",
    )

    def get_name(self, obj):
        return obj.tshirt.name

    get_name.short_description = "T-Shirt Name"

    def get_album(self, obj):
        return obj.tshirt.album

    get_album.short_description = "Associated Album"

    def get_image(self, obj):
        if obj.tshirt.image:
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.tshirt.image.url,
                    width=50,
                    height=50,
                )
            )
        else:
            return "No Image"

    get_image.short_description = "Image"
