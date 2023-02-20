from rest_framework import viewsets
from apps.services.models import Service
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.services.api.serializers import ServiceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser


class ServiceList(APIView):
    def get(self, request):
        serializer = ServiceSerializer()
        service = Service.objects.all()
        response, status = serializer.get_service(service)
        return Response(response, status)

    def post(self, request):    
        serializer = ServiceSerializer()
           
        response, status = self.create_service(request)
        return Response(response, status)