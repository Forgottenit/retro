# Generated by Django 4.2.2 on 2023-07-15 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0018_alter_review_review_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlbumRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("artist_name", models.CharField(max_length=200)),
                ("album_title", models.CharField(max_length=200)),
                ("message", models.TextField(blank=True, null=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.customer",
                    ),
                ),
            ],
        ),
    ]
