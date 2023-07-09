from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class Customer(models.Model):
    """
    Model representing a customer user for maintaining default
    delivery information and order history
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    default_first_name = models.CharField(
        max_length=150, null=False, blank=False
    )
    default_last_name = models.CharField(
        max_length=150, null=False, blank=False
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

    def __str__(self):
        """
        Return the username.
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Customer.objects.create(user=instance)
    # Existing users: just save the profile
    instance.customer.save()


class Staff(models.Model):
    """
    Model representing a staff user.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="staff"
    )
    role = models.ForeignKey("Role", on_delete=models.CASCADE)
    hire_date = models.DateField()

    def __str__(self):
        """
        Return the username.
        """
        return str(self.user)


class Role(models.Model):
    """
    Model representing a role for staff members.
    """

    role_name = models.CharField(max_length=255)

    def __str__(self):
        """
        Return role.
        """
        return str(self.role_name)
