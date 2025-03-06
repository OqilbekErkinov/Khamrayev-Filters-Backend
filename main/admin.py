from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth.models import User, Group
from main import models

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(models.Filter_type)
class Filter_type(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'parent',
    )

@admin.register(models.Manafacturer)
class Manafacturer(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image',
    )

@admin.register(models.Brands_of_equipment)
class Brands_of_equipment(ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

@admin.register(models.Equipment)
class Equipment(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image',
    )

@admin.register(models.Oil_filter)
class Oil_filter(ModelAdmin):
    list_display = (
        'firm',
        'article_number',
        'type',
        'description',
        'bp_opening_dp',
        'inner_gasket_diameter',
        'largest_od',
        'efficiency',
        'gasket_hd',
        'length',
        'outer_seam_diameter',
        'stock',
        'image',
        'slug',
    )

