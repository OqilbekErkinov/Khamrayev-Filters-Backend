# Generated by Django 5.1.6 on 2025-03-07 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_brands_of_equipment_slug_alter_equipment_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter_type',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('specifications', models.JSONField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='oil_filters/')),
                ('slug', models.SlugField(unique=True)),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manafacturers', to='main.manafacturer')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_types', to='main.filter_type')),
            ],
        ),
        migrations.DeleteModel(
            name='Oil_filter',
        ),
    ]
