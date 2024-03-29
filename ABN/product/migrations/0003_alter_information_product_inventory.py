# Generated by Django 5.0.1 on 2024-01-26 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_information_product_inventory_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information_product",
            name="inventory",
            field=models.PositiveIntegerField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="موجودی محصول",
            ),
        ),
    ]
