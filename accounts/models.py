from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Model representing a customer user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                related_name='customer')
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        """
        Return the username.
        """
        return str(self.user)


class Staff(models.Model):
    """
    Model representing a staff user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                related_name='staff')
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
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
        return self.role_name
