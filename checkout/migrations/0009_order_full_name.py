# Generated by Django 4.2.2 on 2023-07-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0008_remove_order_full_name_alter_order_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="full_name",
            field=models.CharField(default="RER DER", max_length=50),
            preserve_default=False,
        ),
    ]
