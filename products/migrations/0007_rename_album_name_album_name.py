# Generated by Django 4.2.2 on 2023-06-23 18:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_rename_name_album_album_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="album",
            old_name="album_name",
            new_name="name",
        ),
    ]
