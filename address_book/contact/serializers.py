from rest_framework import serializers
from contact.models import Contact, Events
import datetime

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


class ContactFromEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'id']


class EventsSerializer(serializers.ModelSerializer):
    contacts = ContactFromEventsSerializer(many=True)

    def validate_date_time(self, value):
        if value.replace(tzinfo=None) <= datetime.datetime.now().replace(tzinfo=None):
            raise serializers.ValidationError('Заборонено створювати заходи на вже минулі дати')
        return value

    class Meta:
        model = Events
        fields = ['title', 'description', 'date_time', 'location', 'contacts']