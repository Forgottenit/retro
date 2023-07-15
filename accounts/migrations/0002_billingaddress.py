# Generated by Django 4.2.2 on 2023-06-18 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BillingAddress",
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
                    "billing_address_line1",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "billing_address_line2",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "billing_city",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "billing_county",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "billing_postcode",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "billing_country",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing_addresses",
                        to="accounts.customer",
                    ),
                ),
            ],
        ),
    ]
