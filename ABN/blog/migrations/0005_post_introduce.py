# Generated by Django 5.0.1 on 2024-01-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_post_modified"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="introduce",
            field=models.CharField(max_length=200, null=True, verbose_name="معرفی پست"),
        ),
    ]