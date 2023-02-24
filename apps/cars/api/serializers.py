from django.db import transaction

from apps.cars.models import Car


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

    def update_car(self, car, request):
        try:
            with transaction.atomic():
                car.name = request.data.get("name", car.name)
                car.brand = request.data.get("brand", car.brand)
                car.plate = request.data.get("plate", car.plate)  # noqa: E501
                car.year = float(request.data.get("year", car.year))  # noqa: E501
                car.km = float(request.data.get("km", car.km))  # noqa: E501
                car.color = request.data.get("color", car.color)  # noqa: E501

                car.save()
                return {"detail": "Product was updated successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "car could not be changed."}, 400

    def get_all_cars(self, cars):
        car_list_dict = []

        for car in cars:
            car_dict = self.build_car_dict(car)
            car_list_dict.append(car_dict)

        return car_list_dict, 200

    def build_car_dict(self, car):
        car_dict = {
            "name": car.name,
            "brand": car.brand,
            "plate": car.plate,
            "year": car.year,
            "km": car.km,
            "color": car.color
        }
        return car_dict
