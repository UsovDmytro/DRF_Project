from rest_framework import serializers
from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    street = serializers.CharField(max_length=30)
    url = serializers.URLField(max_length=200)
    phone = serializers.CharField(max_length=30)
    image = serializers.ImageField(required=False) # це поле не обов'язкове

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'country', 'city', 'street', 'url', 'phone', 'image']