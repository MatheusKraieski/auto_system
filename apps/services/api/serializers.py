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

                self.add_images_to_service(
                    service, request.data.getlist('images'))

            return {'detail': 'Service created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Service could not be created.'}, 400

    @staticmethod
    def add_images_to_service(service, images):
        for image in images:
            ServiceImage.objects.create(
                service=service,
                image=image,
            )

    def get_service(self, service):
        service_dict = self.build_service_dict(service)
        return service_dict, 200

    def get_all_services(self, services):
        service_list_dict = []

        for service in services:
            services_dict = self.build_service_dict(service)
            service_list_dict.append(services_dict)

        return service_list_dict, 200

    def build_service_dict(self, service):
        service_dict = {
            "ref-code": service.ref_code,
            "description": service.description,
            "observation": service.observation,
            "image": service.images.values(),
            "client": {
                "id": service.client_id,
                "name": service.client.name,
                "first_phone": service.client.first_phone,
            },
            "car": {
                "id": service.car_id,
                "name": service.car.name,
                "color": service.car.color,
                "plate": service.car.plate,
            },
        }

        return service_dict

    def update_service(self, service, request):
        try:
            with transaction.atomic():
                service.observation = request.data.get("observation", service.ref_code)  # noqa: E501
                if request.data:
                    images = request.data.getlist("images")
                    if images:
                        service.images.all().delete()
                        self.add_images_to_service(service, images)

                service.save()
                return {"detail": "Service was updated successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "Service could not be changed."}, 400

    def delete_service(self, service, request):
        try:
            if transaction.atomic():
                service.delete()
            return {"detail": "Service was deleted successfully"}, 201
        except Exception as err:
            print(err)
            return {"error": "Service could not be deleted"}, 400