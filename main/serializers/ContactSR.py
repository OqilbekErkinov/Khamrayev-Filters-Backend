from rest_framework import serializers
from main.models.Contact import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['name', 'phone_number', 'email', 'message']
