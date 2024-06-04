import datetime
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from unaHealt.response import MakeResponse
from rest_framework.views import APIView
from .models import Glucose
from .serializers import LevelsSerializer


class MyCustomPagination(LimitOffsetPagination):
    pass

class Levels(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LevelsSerializer
    pagination_class = MyCustomPagination

    def validate(self):
        try:
            datetime.strptime(self.request.query_params.get('start'), '%Y-%m-%d %H:%M:%S')
            datetime.strptime(self.request.query_params.get('stop'), '%Y-%m-%d %H:%M:%S')
        except:
            raise ValidationError({"error": u'Wrong Date Format'})

    def get_queryset(self):

        queryset = Glucose.objects.all()

        if self.request.query_params.get('start') is not None:
            queryset = queryset.filter(device_timestamp__gt=self.request.query_params.get('start'))
        if self.request.query_params.get('stop') is not None:
            queryset = queryset.filter(device_timestamp__lt=self.request.query_params.get('stop'))

        return queryset


class LevelsByUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LevelsSerializer
    pagination_class = MyCustomPagination

    def validate(self):
        try:
            datetime.strptime(self.request.query_params.get('start'), '%Y-%m-%d %H:%M:%S')
            datetime.strptime(self.request.query_params.get('stop'), '%Y-%m-%d %H:%M:%S')
        except:
            raise ValidationError({"error": u'Wrong Date Format'})

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['id'])
        queryset = Glucose.objects.filter(user=user).all()

        if self.request.query_params.get('start') is not None:
            queryset = queryset.filter(device_timestamp__gt=self.request.query_params.get('start'))
        if self.request.query_params.get('stop') is not None:
            queryset = queryset.filter(device_timestamp__lt=self.request.query_params.get('stop'))

        return queryset

class CreateLevel(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LevelsSerializer

    def post(self, request):
        new_collection = self.serializer_class(data={**request.data, **{'user': request.user.id}},many=False)
        if new_collection.is_valid():
            new_level = new_collection.create(validated_data=new_collection.validated_data)
            return MakeResponse(data=new_level.id, status=200).response()
        else:
            return MakeResponse(data=new_collection.errors, status=404).response()
        return MakeResponse(data=[], status=404).response()