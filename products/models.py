from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class ExternalUrl(models.Model):
    spotify = models.URLField(blank=True, null=True)


class Artist(models.Model):
    artist_name = models.CharField(
        max_length=100, blank=True, null=True, db_index=True
    )
    artist_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
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
        if self.external_urls:
            external_url = self.external_urls
            self.external_urls = None
            self.save()
            external_url.delete()
        super().delete(*args, **kwargs)


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
    uri = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    href = models.URLField(blank=True, null=True)
    external_urls = models.OneToOneField(
        ExternalUrl, on_delete=models.CASCADE, null=True, blank=True
    )
    artists = models.ManyToManyField(Artist, related_name="tracks")

    def __str__(self):
        return self.track_name

        super().delete(*args, **kwargs)


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
    popularity = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(0)]
    )
    album_id = models.CharField(
        max_length=100, unique=True, blank=False, null=False
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
    image_data = models.ForeignKey(
        Image, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("25.00"),
        validators=[MinValueValidator(0)],
    )
    ratings = GenericRelation(Rating, related_query_name="albums")

    def __str__(self):
        return f"{self.album_name}"

    def delete(self, *args, **kwargs):
        artists = self.artists.all()
        if self.image_data:
            image_data = self.image_data
            self.image_data = None
            self.save()
            image_data.delete()

        for artist in artists:
            if artist.albums.count() == 0:
                artist.delete()

        super().delete(*args, **kwargs)


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
        return (
            f"{self.tshirt} - Size: {self.size} - Quantity: {self.quantity}"
        )
