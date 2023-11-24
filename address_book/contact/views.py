from rest_framework import filters, viewsets
from contact.models import Contact, Events
from contact.serializers import ContactSerializer, EventsSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'date_time', 'location']