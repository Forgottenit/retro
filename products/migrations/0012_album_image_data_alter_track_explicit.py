# Generated by Django 4.2.2 on 2023-06-23 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0011_rename_name_album_album"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="image_data",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.image",
            ),
        ),
        migrations.AlterField(
            model_name="track",
            name="explicit",
            field=models.BooleanField(null=True),
        ),
    ]