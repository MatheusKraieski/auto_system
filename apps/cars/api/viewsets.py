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
