# Generated by Django 4.2.2 on 2023-06-28 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_album_tracks_alter_track_album"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="album",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="track_set",
                to="products.album",
            ),
        ),
    ]