# Generated by Django 4.2.2 on 2023-06-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_rename_album_album_name_alter_album_tracks"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="track",
            name="album",
        ),
        migrations.AlterField(
            model_name="album",
            name="tracks",
            field=models.ManyToManyField(related_name="albums", to="products.track"),
        ),
        migrations.DeleteModel(
            name="AlbumArtist",
        ),
    ]