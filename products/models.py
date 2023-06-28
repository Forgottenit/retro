from django.core.validators import MinValueValidator
from django.db import models

EXPLICIT_CHOICES = (
    ("E", "Explicit"),
    ("C", "Clean"),
    ("U", "Unknown"),
)


class ExternalUrl(models.Model):
    spotify = models.URLField(blank=True, null=True)


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
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
        return self.name


class Track(models.Model):
    album = models.ForeignKey(
        "Album",
        related_name="track_set",
        related_query_name="track",  # Update the related_name here
        null=True,
        on_delete=models.CASCADE,
    )
    track_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
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
        return self.name


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
    name = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.CharField(
        max_length=10, blank=True, null=True
    )  # Changed due to differing formats on spotify
    total_tracks = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    album_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    album_type = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    copyrights = models.CharField(max_length=100, blank=True, null=True)
    explicit = models.BooleanField(null=True)
    # explicit = models.CharField(
    #     max_length=1, choices=EXPLICIT_CHOICES, blank=True, null=True
    # )
    genres = models.ManyToManyField(Genre, related_name="albums")
    tracks = models.ManyToManyField(
        Track, related_name="albums", db_table="albums_tracks"
    )
    spotify_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="album_images", blank=True, null=True)
    image_data = models.ForeignKey(
        Image, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.album_id} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="product_images", blank=True, null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


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
