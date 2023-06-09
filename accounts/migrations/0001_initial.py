# Generated by Django 4.2.2 on 2023-06-15 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hire_date", models.DateField()),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.role"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staff",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "default_phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "default_street_address1",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_street_address2",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_town_or_city",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "default_county",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "default_postcode",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "default_country",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
