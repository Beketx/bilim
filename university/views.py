from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from university.models import Specialty, University, Faculty
from university.serializers import SpecialtyDetailedSerializer, SpecialtySerializer, UniversityDetailedSerializer, UniversitySerializer, FacultySerializer, DetailedFacultySerializer


class UniversityView(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = University.objects.all()

    def list(self, request):
        serializer = UniversitySerializer(self.queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        university = self.get_object()
        serializer = UniversityDetailedSerializer(university)

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

    #TODO: Список универов При клике на обьект показывает -> Список професси каждого уника и проф предметы
    @action(methods=['GET'], detail=False)
    def f(self, request):
        faculty = Faculty.objects.all()
        serializer = DetailedFacultySerializer(faculty, many=True)
        print(serializer)
        return Response(serializer.data)

class SpecialtyView(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Specialty.objects.all()

    def list(self, request):
        serializer = SpecialtySerializer(self.queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        faculty = self.get_object()
        serializer = SpecialtyDetailedSerializer(faculty)

        return Response(serializer.data)
    # def retrieve(self, request):
    #     uni_id = request.GET.get('uni_id')
    #     spec_id = request.GET.get('spec_id')
    #     university = University.objects.filter(id=uni_id).first()
    #     faculty = Faculty.objects.get(university=university)
    #     specialty = Specialty.objects.filter()
    #     serializer = SpecialtyDetailedSerializer(self.queryset, many=True)

    #     return Response(serializer.data)