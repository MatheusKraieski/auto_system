from django.urls import path
from apps.services.api import viewsets


urlpatterns = [
    path('service', viewsets.ServiceList.as_view()),
]