from django.urls import path, include
from .views import ContactViewSet, EventsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'events', EventsViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]