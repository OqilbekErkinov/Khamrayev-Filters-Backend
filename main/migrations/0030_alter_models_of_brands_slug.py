# Generated by Django 5.1.6 on 2025-03-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_models_of_brands_products_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models_of_brands',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
