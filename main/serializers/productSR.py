from rest_framework import serializers
from main import models
from main.models import SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'alt_name', 'type', 'slug']

class ProductsSerializer(serializers.ModelSerializer):
    firm = serializers.CharField(source='firm.name')
    type = serializers.CharField(source='type.name')
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = models.Products
        fields = ['id', 'firm', 'article_number', 'type', 'subcategory', 'description',
                  'specifications', 'image', 'slug', 'created_at', 'updated_at'
                  ]




class Filter_typeSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = models.Filter_types
        fields = ['id', 'name', 'slug', 'stock', 'subcategories', 'available', 'svg']



class ManafacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manafacturers
        fields = ['id', 'name', 'slug', 'image', 'available']


class Brands_of_equipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brands_of_equipments
        fields = ['id', 'name', 'slug', 'available']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipments
        fields = ['id', 'name', 'slug', 'image', 'available']
