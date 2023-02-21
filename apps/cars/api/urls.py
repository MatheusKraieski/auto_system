from django.urls import path

from apps.cars.api import viewsets

urlpatterns = [
    path('cars', viewsets.CarList.as_view()),
]