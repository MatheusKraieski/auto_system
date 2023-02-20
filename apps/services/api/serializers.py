from typing import List

from django.db import transaction
from rest_framework import serializers

from apps.services.models import Service, ServiceImage


class ServiceSerializer(serializers.ModelSerializer):
    def create_service(self, request, car, client):
        try:
            with transaction.atomic():
                service = Service.objects.create(
                    ref_code=request.data.get("ref_code"),
                    client_id=request.data.get("client_id"),
                    car_id=request.data.get('car_id'),
                    description=request.data.get("description"),
                    observation=request.data.get('observation'),
                )

                self.add_images_to_product(
                    service, request.data.getlist('images'))

            return {'detail': 'Service created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Service could not be created.'}, 400

    @staticmethod
    def add_images_to_product(service, images):
        for image in images:
            ServiceImage.objects.create(
                service=service,
                image=image,
            )

    def get_service(self, service):
        service_dict = self.build_service_dict(service)
        return service_dict, 200

    def build_service_dict(self, services: List[Service]):
        service_dict = []
        for service in services:
            service_dict = {
                "ref-code": service.ref_code,
                "client_id": service.client_id,
                "car_id": service.car_id,
                "description": service.description,
                "observation": service.observation,
                "image": service.images.values(),
            }

        return service_dict
