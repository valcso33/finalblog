# Generated by Django 5.0.4 on 2024-05-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_tag_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
