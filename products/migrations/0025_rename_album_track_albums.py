# Generated by Django 4.2.2 on 2023-06-30 12:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0024_rename_name_artist_artist_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="track",
            old_name="album",
            new_name="albums",
        ),
    ]
