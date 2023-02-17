from rest_framework import serializers
from apps.services.models import Service
from django.db import transaction



class ServiceSerializer(serializers.ModelSerializer):
    def add_client(self, request):
        try:
            with transaction.atomic():
                service = Service.objects.create(
                    client=request.data.get('client'),
                    car=request.data.get('car'),
                    description=request.data.get("description"),
                    observation=request.data.get('observation'),
                )

                self.add_images_to_product(service, request.data.getlist('images'))

            return {'detail': 'Service created successfully.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Service could not be created.'}, 400
    
    def get_service(self, service):
        service_dict = self.build_service_dict(service)
        return service_dict, 200
    
    def build_service_dict(self, service):
        service_dict = {
            "id": service.pk,
            "name": service.name,
            "category_id": service.category_id,
            "cost": service.cost,
            "inventory_number": service.inventory_number,
            "favorite": service.favorite,
            "image": service.images.values(),
            "categories": []
        }

        for category in product_categories:
            product_dict["categories"].append(self.build_category_dict(category))

        return product_dict
