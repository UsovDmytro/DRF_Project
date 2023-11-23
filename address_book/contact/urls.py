from django.urls import path
from .views import ContactList, ContactDetail


urlpatterns = [
    path('contacts/', ContactList.as_view()),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
]