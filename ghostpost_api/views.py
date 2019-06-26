from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import BoastOrRoast
from .serializers import BoastOrRoastSerializer


class AllPostsViewSet(viewsets.ModelViewSet):
    queryset = BoastOrRoast.objects.all()
    serializer_class = BoastOrRoastSerializer

    # def create(self, request, *args, **kwargs):
    #     BoastOrRoast.objects.create(request.data)


class BoastViewSet(viewsets.ModelViewSet):
    serializer_class = BoastOrRoastSerializer
    queryset = BoastOrRoast.objects.filter(title='b')


class RoastViewSet(viewsets.ModelViewSet):
    serializer_class = BoastOrRoastSerializer
    queryset = BoastOrRoast.objects.filter(title='r')
