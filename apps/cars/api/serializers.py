from apps.cars.models import Car
from django.db import transaction


class CarSerializer:
    def create_car(self, request):
        try:
            with transaction.atomic():
                car = Car.objects.create(
                    name=request.data.get('name'),
                    brand=request.data.get("brand"),
                    plate=request.data.get('plate'),
                    year=request.data.get('year'),
                    km=request.data.get('km'),
                    color=request.data.get('color'),                    
                )

            return {"detail": "Car created successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "Car could not be created."}, 400
