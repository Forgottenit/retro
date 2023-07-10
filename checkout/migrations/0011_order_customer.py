# Generated by Django 4.2.2 on 2023-07-10 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0011_rename_default_first_name_customer_default_full_name_and_more",
        ),
        ("checkout", "0010_remove_order_customer_remove_order_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="accounts.customer",
            ),
        ),
    ]
