# Generated by Django 5.0.1 on 2024-01-26 19:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_information_product_introduce"),
    ]

    operations = [
        migrations.AddField(
            model_name="information_product",
            name="description_2",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name="توضحیات 2  محصول"
            ),
        ),
    ]
