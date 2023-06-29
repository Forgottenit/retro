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
    # AlbumArtist,
)
from django.utils.safestring import mark_safe


# class TrackInline(admin.TabularInline):
#     model = Track
#     extra = 1
#     classes = ("collapse",)


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
    list_display = (
        "name",
        "display_artists",
        "album",
        "track_number",
        "duration",
        "explicit",
    )
    list_filter = ("name",)
    search_fields = ("name", "album__album_id")
    autocomplete_fields = ("album",)

    def display_artists(self, obj):
        return ", ".join([str(artist) for artist in obj.artists.all()])

    display_artists.short_description = "Artists"

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term
        )
        queryset |= self.model.objects.filter(
            artists__name__icontains=search_term
        )
        return queryset, use_distinct


# class AlbumArtistInline(admin.TabularInline):
#     model = AlbumArtist
#     extra = 1


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
    # list_select_related = ("albums",)
    # inlines = [AlbumArtistInline]

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = "Genres"

    def get_albums(self, obj):
        return ", ".join([album.name for album in obj.albums.all()])

    get_albums.short_description = "Albums"

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.prefetch_related("albums")
    #     return queryset

    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super().get_search_results(
    #         request, queryset, search_term
    #     )
    #     if search_term:
    #         album_results = Album.objects.filter(name__icontains=search_term)
    #         queryset = queryset | self.model.objects.filter(
    #             albums__in=album_results
    #         )
    #     return queryset, use_distinct


@admin.register(Album)
class AlbumAdmin(ImageDisplayMixin, admin.ModelAdmin):
    # inlines = [TrackInline, AlbumArtistInline]

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
