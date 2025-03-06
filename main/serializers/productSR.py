from rest_framework import serializers
from main import models

class Oil_filterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Oil_filter
        fields = ['id', 'firm', 'article_number', 'type', 'description',
                  'bp_opening_dp', 'inner_gasket_diameter', 'largest_od',
                  'efficiency', 'gasket_hd', 'length',
                  'outer_seam_diameter', 'stock', 'image', 'slug'
                  ]

class Filter_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filter_type
        fields = ['id', 'name', 'slug', 'parent']

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