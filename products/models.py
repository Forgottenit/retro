from django.core.validators import MinValueValidator
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    artist_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    genres = models.ManyToManyField("Genre")
    spotify_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Track(models.Model):
    track_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    explicit = models.BooleanField(blank=True, null=True)
    spotify_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    release_date = models.DateField(blank=True, null=True)
    total_tracks = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    album_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    album_type = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    copyright = models.CharField(max_length=100, blank=True, null=True)
    explicit = models.BooleanField(blank=True, null=True)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)
    tracks = models.ManyToManyField(Track)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
    )
    on_sale = models.BooleanField(blank=True, null=True, default=False)
    spotify_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="album_images", blank=True, null=True)

    def __str__(self):
        return self.album_id


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
    )
    on_sale = models.BooleanField(blank=True, null=True, default=False)
    image = models.ImageField(
        upload_to="product_images", blank=True, null=True
    )

    def __str__(self):
        return self.name


class CD(Product):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"CD: {self.album}"


class Vinyl(Product):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vinyl: {self.album}"


class TShirtSize(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class TShirt(Product):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(TShirtSize)

    def __str__(self):
        return f"T-Shirt: {self.album}"


class TShirtQuantity(models.Model):
    tshirt = models.ForeignKey(TShirt, on_delete=models.CASCADE)
    size = models.ForeignKey(TShirtSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.tshirt} - {self.size}: {self.quantity}"
