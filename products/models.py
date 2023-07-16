from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


# class ExternalUrl(models.Model):
#     spotify = models.URLField(blank=True, null=True)


class Artist(models.Model):
    artist_name = models.CharField(
        max_length=100, blank=True, null=True, db_index=True
    )
    artist_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    genres = models.ManyToManyField("Genre")
    spotify_url = models.URLField(blank=True, null=True)
    # uri = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)
    # external_urls = models.OneToOneField(
    #     ExternalUrl, on_delete=models.CASCADE, null=True, blank=True
    # )

    def delete(self, *args, **kwargs):
        # Delete the associated URLs
        # if self.external_urls:
        #     self.external_urls.delete()

        # Delete the associated tracks
        tracks_to_delete = list(self.tracks.all())
        for track in tracks_to_delete:
            track.artists.remove(self)
            if track.artists.count() == 0:
                track.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.artist_name


class Track(models.Model):
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
    # uri = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)
    # external_urls = models.OneToOneField(
    #     ExternalUrl, on_delete=models.CASCADE, null=True, blank=True
    # )
    artists = models.ManyToManyField(Artist, related_name="tracks")

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.track_name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Image(models.Model):
#     height = models.IntegerField(blank=True, null=True)
#     width = models.IntegerField(blank=True, null=True)
#     url = models.URLField(blank=True, null=True)


class Album(models.Model):
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
    )  # Changed due to differing formats on spotify
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
    # image_data = models.ForeignKey(
    #     Image, on_delete=models.CASCADE, null=True, blank=True
    # )
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
        return f"{self.album_name}"


# class Product(models.Model):
#     product_name = models.CharField(max_length=100, null=True)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(
#         upload_to="product_images", blank=True, null=True
#     )

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.product_name
