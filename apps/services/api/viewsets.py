from rest_framework import viewsets
from apps.clients.models import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.clients.api.serializers import ClientSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser


class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.values(request)
        return Response(clients, 200)

    def post(self, request):    
        serializer = ClientSerializer()
           
        response, status = serializer.add_client(request)
        return Response(response, status)