# Generated by Django 4.2.2 on 2023-07-07 22:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_billingaddress"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BillingAddress",
        ),
    ]
