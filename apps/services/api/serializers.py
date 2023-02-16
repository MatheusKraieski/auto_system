from rest_framework import serializers
from apps.clients.models import Client
from django.db import transaction



class ClientSerializer(serializers.ModelSerializer):
    def add_client(self, request):
        try:
            Client.objects.create(
                client=request.data.get('client'),
                car=request.data.get('car'),
                description=request.data.get("description"),
                cnpj=request.data.get('cnpj'),
                observation=request.data.get('observation'),
            )

            return {'detail': 'Service created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Service could not be created.'}, 400   