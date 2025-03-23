from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User, Group
from main import models
from main.models.FilterSearch import FilterRequest
from main.models.Contact import ContactForm
from main.models.Oformit import OformitProducts, OformitProductItem
from main.models import SubCategory


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(models.SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ('name', 'alt_name', 'type', 'slug')
    prepopulated_fields = {'slug': ('type',)}

@admin.register(models.Filter_types)
class Filter_typesAdmin(ModelAdmin):
    list_display = (
        'name',
        'slug',
        'stock',
        'display_subcategories',
        'available',
        'svg',
    )
    filter_horizontal = ('subcategories',)

    def display_subcategories(self, obj):
        """ ManyToManyField qiymatlarini string sifatida chiqarish """
        return ", ".join([subcategory.name for subcategory in obj.subcategories.all()])

    display_subcategories.short_description = "Subcategories"



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
        'subcategory',
        'description',
        'specifications',
        'image',
        'slug',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {'slug': ('article_number',)}




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