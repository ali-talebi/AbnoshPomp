# Generated by Django 5.0.1 on 2024-01-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0010_product_comment_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="product_comment",
            name="creation",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="زمان "
            ),
        ),
    ]