from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clients.api.serializers import ClientSerializer
from apps.clients.models import Client


class ClientList(APIView):
    serializer = ClientSerializer()
    def get(self, request):
        client = Client.objects.all()
        response, status = self.serializer.get_all_clients(client)
        return Response(response, status)

    def post(self, request):        
        response, status = self.serializer.add_client(request)
        return Response(response, status)
