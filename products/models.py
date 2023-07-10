from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db.models import Count
import os
from django.conf import settings

EXPLICIT_CHOICES = (
    ("E", "Explicit"),
    ("C", "Clean"),
    ("U", "Unknown"),
)


class ExternalUrl(models.Model):
    spotify = models.URLField(blank=True, null=True)


class Artist(models.Model):
    artist_name = models.CharField(
        max_length=100, blank=True, null=True, db_index=True
    )
    artist_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    # albums = models.ManyToManyField("Album", through="AlbumArtist")

    genres = models.ManyToManyField("Genre")

    spotify_url = models.URLField(blank=True, null=True)
    uri = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)
    external_urls = models.OneToOneField(
        ExternalUrl, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.artist_name

    def delete(self, *args, **kwargs):
        # If this artist has an associated ExternalUrl
        if self.external_urls:
            external_url = self.external_urls
            self.external_urls = None  # nullify the relationship
            self.save()  # save the artist to update the foreign key
            external_url.delete()  # then delete the ExternalUrl
        super().delete(*args, **kwargs)  # Call the "real" delete() method.


class Track(models.Model):
    albums = models.ForeignKey(
        "Album",
        related_name="tracks",  # updated related_name
        null=True,
        on_delete=models.CASCADE,
    )
    track_number = models.IntegerField(blank=True, null=True)
    track_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    explicit = models.BooleanField(null=True)
    spotify_url = models.URLField(blank=True, null=True)
    uri = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)
    external_urls = models.OneToOneField(
        ExternalUrl, on_delete=models.CASCADE, null=True, blank=True
    )
    artists = models.ManyToManyField(Artist, related_name="tracks")

    def __str__(self):
        return self.track_name

    def delete(self, *args, **kwargs):
        # If this track has an associated ExternalUrl
        if self.external_urls:
            external_url = self.external_urls
            self.external_urls = None  # nullify the relationship
            self.save()  # save the track to update the foreign key
            external_url.delete()  # then delete the ExternalUrl
        super().delete(*args, **kwargs)  # Call the "real" delete() method.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)


class Album(models.Model):
    artists = models.ManyToManyField(Artist, related_name="albums")
    artist_id = models.CharField(max_length=100, blank=True, null=True)
    album_name = models.CharField(
        max_length=100, blank=True, null=True, db_index=True
    )
    release_date = models.CharField(
        max_length=10, blank=True, null=True
    )  # Changed due to differing formats on spotify
    total_tracks = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    album_id = models.CharField(
        max_length=100, unique=True, blank=False, null=False
    )
    album_type = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    copyrights = models.CharField(max_length=500, blank=True, null=True)
    explicit = models.BooleanField(null=True)
    # explicit = models.CharField(
    #     max_length=1, choices=EXPLICIT_CHOICES, blank=True, null=True
    # )
    genres = models.ManyToManyField(
        Genre, related_name="albums", db_index=True
    )
    spotify_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="album_images", blank=True, null=True)
    image_data = models.ForeignKey(
        Image, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=Decimal("25.00")
    )

    def __str__(self):
        return f"{self.album_name}"

    def delete(self, *args, **kwargs):
        # Get all artists associated with the album
        artists = self.artists.all()

        # If album has an associated image
        if self.image:
            self.image.delete()

        super().delete(*args, **kwargs)  # Call the "real" delete() method

        for artist in artists:  # Check each artist
            if artist.albums.count() == 0:  # If the artist has no other albums
                artist.delete()  # Delete the artist


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="product_images", blank=True, null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.product_name


class CD(Product):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"CD: {self.album}"


class Vinyl(Product):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"Vinyl: {self.album}"


class TShirtSize(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class TShirt(Product):
    SLEEVE_CHOICES = [("short", "Short"), ("long", "Long")]

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    sleeve_length = models.CharField(
        max_length=5, choices=SLEEVE_CHOICES, default="short"
    )
    colour = models.CharField(max_length=100, blank=True, null=True)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"T-Shirt: {self.album}"


class TShirtVariant(models.Model):
    tshirt = models.ForeignKey(TShirt, on_delete=models.CASCADE)
    size = models.ForeignKey(TShirtSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tshirt} - Size: {self.size} - Quantity: {self.quantity}"


# SIGNAL PREDELETE FOR CUSTOM SEARCH DELETES


@receiver(pre_delete, sender=Album)
def delete_related_objects(sender, instance, **kwargs):
    # Get all artists that only are on this album (to be deleted).
    artists_to_delete = instance.artists.annotate(
        album_count=Count("albums")
    ).filter(album_count=1)
    # Delete all tracks associated with this album.
    instance.tracks.all().delete()
    # Delete the artists that are only on this album.
    artists_to_delete.delete()


@receiver(pre_delete, sender=Artist)
def delete_related_albums(sender, instance, **kwargs):
    # Get all albums associated with this artist
    albums_to_delete = instance.albums.all()
    for album in albums_to_delete:
        # Need to remove the artist from the album before deleting to prevent recursion
        album.artists.remove(instance)
        # Check if this album has other artists associated, if not, delete it
        if album.artists.count() == 0:
            album.delete()
