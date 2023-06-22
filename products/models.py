from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    artist_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    genres = models.TextField(blank=True, null=True)
    spotify_url = models.URLField(blank=True, null=True)

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
    tracks = models.ManyToManyField(Track)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    on_sale = models.BooleanField(blank=True, null=True, default=False)
    spotify_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="album_images", blank=True, null=True)

    def __str__(self):
        return self.album_id
