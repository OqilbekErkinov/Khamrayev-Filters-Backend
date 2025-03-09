from rest_framework import serializers
from main import models

class ProductsSerializer(serializers.ModelSerializer):
    firm = serializers.CharField(source='firm.name')
    type = serializers.CharField(source='type.name')
    class Meta:
        model = models.Products
        fields = ['id', 'firm', 'article_number', 'type', 'description',
                  'specifications', 'image', 'slug'
                 ]

class Filter_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter_type
        fields = ['id', 'name', 'slug', 'stock', 'parent']

class ManafacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter_type
        fields = ['id', 'name', 'slug', 'image']

class Brands_of_equipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter_type
        fields = ['id', 'name', 'slug']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter_type
        fields = ['id', 'name', 'slug', 'image']