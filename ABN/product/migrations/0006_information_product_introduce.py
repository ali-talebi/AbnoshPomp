# Generated by Django 5.0.1 on 2024-01-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_information_product_price2"),
    ]

    operations = [
        migrations.AddField(
            model_name="information_product",
            name="introduce",
            field=models.CharField(
                max_length=100, null=True, verbose_name="توضیحات تک خطی"
            ),
        ),
    ]
