from django.urls import path
from apps.services.api import viewsets


urlpatterns = [
    path('services', viewsets.ServiceList.as_view(), name='services'),
]