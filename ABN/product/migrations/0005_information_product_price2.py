# Generated by Django 5.0.1 on 2024-01-26 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_information_product_showing"),
    ]

    operations = [
        migrations.AddField(
            model_name="information_product",
            name="price2",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=12,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]