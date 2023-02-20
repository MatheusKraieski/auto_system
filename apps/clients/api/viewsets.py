from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clients.api.serializers import ClientSerializer
from apps.clients.models import Client


class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.values()
        return Response(clients, 200)

    def post(self, request):
        serializer = ClientSerializer()
        response, status = serializer.add_client(request)
        return Response(response, status)
