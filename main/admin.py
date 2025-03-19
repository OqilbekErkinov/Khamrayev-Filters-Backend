from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User, Group
from main import models
from main.models.FilterSearch import FilterRequest
from main.models.Contact import ContactForm
from main.models.Oformit import OformitProducts, OformitProductItem

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

@admin.register(FilterRequest)
class FilterRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'message', 'created_at']
    search_fields = ['name', 'email', 'phone_number']


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'message', 'created_at']
    search_fields = ['name', 'email', 'phone_number']


@admin.register(OformitProducts)
class OformitProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address', 'get_products', 'created_at']
    search_fields = ['name', 'email', 'phone_number']

    def get_products(self, obj):
        return ", ".join([f"{item.product.article_number} ({item.product.type}, {item.product.firm})" for item in
                          OformitProductItem.objects.filter(oformit=obj)])

    get_products.short_description = "Ordered Products"