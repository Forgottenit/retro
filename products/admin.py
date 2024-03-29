"""
Module for Products app admin, for Tracks, Artist, Album and Genres
"""

from django.contrib import admin
from django.db import models
from .models import (
    Album,
    Artist,
    Genre,
    Track,
)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    """
    Admin for Tracks
    """

    list_display = (
        "track_name",
        "display_artists",
        "albums",
        "track_number",
        "duration",
        "explicit",
        "spotify_url",
    )
    list_filter = ("track_name",)
    search_fields = ("track_name", "albums__album_id")
    autocomplete_fields = ("albums",)
    ordering = ("track_name",)

    def display_artists(self, obj):
        """
        Admin for joining multiple Artists
        """
        return ", ".join([str(artist) for artist in obj.artists.all()])

    display_artists.short_description = "Artists"

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(
            request, queryset, search_term
        )
        queryset |= self.model.objects.filter(
            artists__artist_name__icontains=search_term
        )
        return queryset, use_distinct


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """
    Admin for Artist
    """

    list_display = (
        "artist_name",
        "artist_id",
        "get_genres",
        "get_albums",
        "spotify_url",
        "type",
    )
    ordering = ("artist_name",)
    list_filter = ("artist_name",)
    search_fields = ("artist_name", "artist_id")

    def get_genres(self, obj):
        """
        Admin for joining multiple Genres
        """
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = "Genres"

    def get_albums(self, obj):
        """
        Admin for joining multiple Albums
        """
        return ", ".join([album.album_name for album in obj.albums.all()])

    get_albums.short_description = "Albums"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """
    Admin for Albums
    """

    list_display = (
        "album_name",
        "display_artists",
        "main_artist",
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
    )
    search_fields = (
        "album_id",
        "main_artist",
        "label",
        "album_name",
        "artist_id",
        "artists__artist_name",
    )
    ordering = ("album_name",)

    def display_artists(self, obj):
        """
        Admin for joining multiple Artists
        """
        return ", ".join([str(artist) for artist in obj.artists.all()])

    def display_genres(self, obj):
        """
        Admin for joining multiple Genres
        """
        return ", ".join([str(genre) for genre in obj.genres.all()])

    def display_tracks(self, obj):
        """
        Admin for joining multiple Tracks
        """
        return ", ".join(
            [str(track.track_name) for track in obj.tracks.all()]
        )

    def get_queryset(self, request):
        query_s = super().get_queryset(request)
        return query_s.annotate(
            artist_name=models.F("artists__artist_name")
        ).order_by("artist_name")

    display_genres.short_description = "Genres"
    display_tracks.short_description = "Tracks"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Admin for Genres
    """

    list_display = ("name",)
    search_fields = ("name",)
