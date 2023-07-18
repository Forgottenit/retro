"""
Module for Product app models, Artist, Track, Genre and Album
"""
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class Artist(models.Model):
    """
    Model for Artist
    """

    artist_name = models.CharField(
        max_length=100, blank=True, null=True, db_index=True
    )
    artist_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    genres = models.ManyToManyField("Genre")
    spotify_url = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)

    def delete(self, *args, **kwargs):
        # Delete the associated tracks
        tracks_to_delete = list(self.tracks.all())
        for track in tracks_to_delete:
            track.artists.remove(self)
            if track.artists.count() == 0:
                track.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        """
        Return Artist name
        """
        return self.artist_name


class Track(models.Model):
    """
    Model for Tracks
    """

    albums = models.ForeignKey(
        "Album",
        related_name="tracks",
        null=True,
        on_delete=models.CASCADE,
    )
    track_number = models.IntegerField(blank=True, null=True)
    track_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    explicit = models.BooleanField(null=True)
    spotify_url = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)

    artists = models.ManyToManyField(Artist, related_name="tracks")

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        """
        Return Track name
        """
        return self.track_name


class Genre(models.Model):
    """
    Model for Genres
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return Genre name
        """
        return self.name


class Album(models.Model):
    """
    Model for Albums
    """

    artists = models.ManyToManyField(Artist, related_name="albums")
    artist_id = models.CharField(max_length=100, blank=True, null=True)
    album_name = models.CharField(
        max_length=100, blank=True, null=True, db_index=True
    )
    main_artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="main_albums",
    )
    release_date = models.CharField(
        max_length=10, blank=True, null=True
    )  # Changed due to inconsistant formats on spotify
    total_tracks = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)]
    )
    album_id = models.CharField(
        max_length=200, unique=True, blank=False, null=False
    )
    album_type = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    copyrights = models.CharField(max_length=500, blank=True, null=True)
    explicit = models.BooleanField(null=True)
    genres = models.ManyToManyField(
        Genre, related_name="albums", db_index=True
    )
    spotify_url = models.URLField(blank=True, null=True)
    image = models.ImageField(
        upload_to="album_images", blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("25.00"),
        validators=[MinValueValidator(0)],
    )
    ratings = GenericRelation(Rating, related_query_name="albums")

    def delete(self, *args, **kwargs):
        artists = self.artists.all()

        # Delete the associated tracks
        tracks_to_delete = list(self.tracks.all())
        for track in tracks_to_delete:
            track.artists.remove(*artists)
            if track.artists.count() == 0:
                track.delete()

        # Delete the album
        super().delete(*args, **kwargs)

        # Delete artists with no remaining albums
        for artist in artists:
            if artist.albums.count() == 0:
                artist.delete()

    def __str__(self):
        """
        Return Album name
        """
        return f"{self.album_name}"
