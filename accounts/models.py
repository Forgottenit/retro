"""
This module defines models Customer,Wishlist, Likes, Reviews
and Album Requests

"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from products.models import Album


class Customer(models.Model):
    """
    Model for Customer
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    default_first_name = models.CharField(
        max_length=150, null=True, blank=True
    )
    default_last_name = models.CharField(
        max_length=150, null=True, blank=True
    )
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label="Country", null=True, blank=True
    )

    @property
    def default_full_name(self):
        """
        Return the default fullname.
        """
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        """
        Return the username.
        """
        return self.user.username if self.user.username else self.user.email


class Like(models.Model):
    """
    Model for Album "Likes"
    """

    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    class Meta:
        """
        Meta class setting uniqueness of Like between
        customer and albums, i.e. Customer can only like an album once
        """

        unique_together = (
            "user",
            "album",
        )


class Wishlist(models.Model):
    """
    Model for Customer Wishlist
    """

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="wishlists"
    )
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class setting uniqueness of wishlist between
        customer and albums, i.e. Customer can only have
        one of album in wishlist
        """

        unique_together = (
            "customer",
            "album",
        )


class Review(models.Model):
    """
    Model for reviews by customers.
    """

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="reviews"
    )
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="reviews"
    )
    review_text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return version of review text with elipses if
        over 75 characters
        """
        if self.review_text is not None:
            review_text_str = str(self.review_text)
            return (
                review_text_str[:75] + "..."
                if len(review_text_str) > 75
                else review_text_str
            )
        else:
            return "Review text is None"


@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    """
    Create or update the Customer profile whenever a User instance is saved.
    """
    if created:
        Customer.objects.create(user=instance)
    # for existing users, just save the profile
    instance.customer.save()


class AlbumRequest(models.Model):
    """
    Model representing album requests by customers.
    """

    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
    )
    request_title = models.CharField(max_length=200, blank=False, null=False)
    artist_name = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request: {self.album_title} by {self.artist_name}"
