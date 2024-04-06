from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from form.models import Review, Client, Student
from form.serializers import ReviewCreateSerializer, ClientCreateSerializer, StudentCreateSerializer, \
    ReviewListSerializer


class ReviewCreateListView(mixins.CreateModelMixin,mixins.ListModelMixin, GenericViewSet):
    queryset = Review.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return ReviewListSerializer


class ClientCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [AllowAny]


class StudentCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [AllowAny]