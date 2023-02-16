from django.urls import path
from apps.cars.api import viewsets


urlpatterns = [
    path('car', viewsets.CarList.as_view()),
]