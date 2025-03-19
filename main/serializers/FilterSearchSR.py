from rest_framework import serializers
from main.models.FilterSearch import FilterRequest


class FilterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterRequest
        fields = ['name', 'phone_number', 'email', 'message']
