# Generated by Django 4.2.2 on 2023-06-29 17:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0021_delete_albumartist"),
    ]

    operations = [
        migrations.RenameField(
            model_name="album",
            old_name="name",
            new_name="album_name",
        ),
    ]