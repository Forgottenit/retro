# Generated by Django 4.2.2 on 2023-06-28 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0012_album_image_data_alter_track_explicit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="album",
            name="tracks",
        ),
        migrations.AddField(
            model_name="track",
            name="album",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tracks",
                to="products.album",
            ),
        ),
    ]
