from django.contrib import admin
from django.db import models
from .models import (
    Album,
    Artist,
    Genre,
    Track,
    CD,
    Vinyl,
    TShirt,
    TShirtVariant,
    Image,
)
from django.utils.safestring import mark_safe


class TrackInline(admin.TabularInline):
    model = Track
    extra = 1
    classes = ("collapse",)


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


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("name", "album", "track_number", "duration", "explicit")
    list_filter = ("name",)
    search_fields = ("name", "album__album_id")
    autocomplete_fields = ("album",)


class AlbumArtist(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class AlbumInline(admin.TabularInline):
    model = AlbumArtist
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "artist_id",
        "get_genres",
        "get_albums",
        "spotify_url",
        "type",
    )
    list_filter = ("name",)
    search_fields = ("name", "artist_id")
    inlines = [AlbumInline]

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = "Genres"

    def get_albums(self, obj):
        return ", ".join([album.name for album in obj.albums.all()])

    get_albums.short_description = "Albums"


@admin.register(Album)
class AlbumAdmin(ImageDisplayMixin, admin.ModelAdmin):
    inlines = [TrackInline]
    list_display = (
        "name",
        "display_artists",
        "artist_id",
        "album_id",
        "release_date",
        "total_tracks",
        "popularity",
        "album_type",
        "label",
        "copyrights",
        "display_genres",
        "explicit",
        "display_tracks",
        "spotify_url",
        "get_image",
    )
    search_fields = (
        "album_id",
        "label",
        "name",
        "artist_id",
        "artists__name",
    )

    def display_artists(self, obj):
        return ", ".join([str(artist) for artist in obj.artists.all()])

    def display_genres(self, obj):
        return ", ".join([str(genre) for genre in obj.genres.all()])

    def display_tracks(self, obj):
        print("Tracks:", obj.tracks.all())
        return ", ".join([str(track.name) for track in obj.tracks.all()])

    def artist_name(self, obj):
        return obj.artists.first().name if obj.artists.exists() else ""

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(artist_name=models.F("artists__name")).order_by(
            "artist_name"
        )

    display_artists.short_description = "Artists"
    display_genres.short_description = "Genres"
    display_tracks.short_description = "Tracks"


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
