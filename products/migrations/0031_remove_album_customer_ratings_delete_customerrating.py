# Generated by Django 4.2.2 on 2023-07-14 21:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0030_customerrating_album_customer_ratings"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="album",
            name="customer_ratings",
        ),
        migrations.DeleteModel(
            name="CustomerRating",
        ),
    ]
