# Generated by Django 4.2.2 on 2023-06-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_rename_album_name_album_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="artist_id",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
