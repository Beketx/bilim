from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from university.models import University, Faculty
from university.serializers import UniversitySerializer, FacultySerializer


class UniversityView(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = University.objects.all()

    def list(self, request):
        serializer = UniversitySerializer(self.queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        university = self.get_object()
        serializer = UniversitySerializer(university)

        return Response(serializer.data)


class FacultyView(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Faculty.objects.all()

    def list(self, request):
        serializer = FacultySerializer(self.queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        faculty = self.get_object()
        serializer = FacultySerializer(faculty)

        return Response(serializer.data)
