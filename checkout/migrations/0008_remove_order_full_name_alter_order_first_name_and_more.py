# Generated by Django 4.2.2 on 2023-07-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0007_order_first_name_order_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="full_name",
        ),
        migrations.AlterField(
            model_name="order",
            name="first_name",
            field=models.CharField(default="R", max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="last_name",
            field=models.CharField(default="D", max_length=30),
            preserve_default=False,
        ),
    ]
