from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.models import Car
from apps.clients.models import Client
from apps.services.api.serializers import ServiceSerializer
from apps.services.models import Service


class ServiceList(APIView):
    def get(self, request):
        serializer = ServiceSerializer()
        service = Service.objects.all()
        response, status = serializer.get_all_services(service)
        return Response(response, status)

    def post(self, request):
        serializer = ServiceSerializer()
        car = Car.objects.get(pk=request.data.get('car_id'))
        client = Client.objects.get(pk=request.data.get('client_id'))
        response, status = serializer.create_service(request, car, client)
        return Response(response, status)
