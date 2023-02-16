from apps.cars.models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.cars.api.serializers import CarSerializer
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404


class CarList(APIView):
    serializer = CarSerializer()
    # parser_classes = (MultiPartParser,)

    def post(self, request):    
                   
        response, status = self.serializer.create_car(request)
        return Response(response, status)