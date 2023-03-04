from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.api.serializers import CarSerializer
from apps.cars.models import Car


class CarList(APIView):
    serializer = CarSerializer()
    # parser_classes = (MultiPartParser,)

    def post(self, request):
        response, status = self.serializer.create_car(request)
        return Response(response, status)

    def get(self, request):
        car = Car.objects.all()
        response, status = self.serializer.get_all_cars(car)
        return Response(response, status)


class CarDetail(APIView):
    parser_classes = (MultiPartParser,)
    serializer = CarSerializer()
    
    def get(self, request, car_pk):
        car = get_object_or_404(Car, pk=car_pk)
        response, status = self.serializer.get_car(car)
        return Response(response, status)

    def put(self, request, car_pk):
        car = get_object_or_404(Car, pk=car_pk)
        response, status = self.serializer.update_car(car, request)
        return Response(response, status)

    def delete(self, request, car_pk):
        car = get_object_or_404(Car, pk=car_pk)
        response, status = self.serializer.delete_car(car)
        return Response(response, status)