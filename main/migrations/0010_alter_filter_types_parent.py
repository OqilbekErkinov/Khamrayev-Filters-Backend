# Generated by Django 5.1.6 on 2025-03-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_filter_types_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_types',
            name='parent',
            field=models.JSONField(default=list),
        ),
    ]
