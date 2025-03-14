from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User, Group
from main import models

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(models.Filter_types)
class Filter_types(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'stock',
        'parent',
        'available',
        'svg',
    )

@admin.register(models.Manafacturers)
class Manafacturers(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image',
        'available',
    )

@admin.register(models.Brands_of_equipments)
class Brands_of_equipments(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'available',
    )

@admin.register(models.Equipments)
class Equipments(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image',
        'available',
    )

@admin.register(models.Products)
class Products(ModelAdmin):
    list_display = (
        'firm',
        'article_number',
        'type',
        'description',
        'specifications',
        'image',
        'slug',
        'created_at',
        'updated_at',
    )