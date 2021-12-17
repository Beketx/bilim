from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from university.models import Specialty, Survey, University, Faculty, UniversityPassPoint
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
    
    @action(detail=False, methods=['post'])
    def survey_save(self, request):
        data = request.data
        user = request.user
        for survey in data['surveys']:
            print(survey)
            Survey.objects.create(user=user, string=survey)
        return Response()
    
    @action(detail=False, methods=['get'])
    def survey_get(self, request):
        user = request.user
        surveys = Survey.objects.filter(user=user)
        if surveys:
            data = []
            for survey in surveys:
                data.append(survey.string)
            json = {
                "surveys":data
            }
            return Response(json)
        return Response()
    
    @action(detail=False, methods=['post'])
    def university_pass(self, request):
        data = request.data
        university_pass = UniversityPassPoint.objects.filter(university_id=data['university'],
                                                            faculty_id=data['faculty'],
                                                            specialty_id=data['specialty']).values_list('pass_point', flat=True)
        avg_point = sum(university_pass)/len(university_pass)
        percent = (data['point'] * 100)/avg_point
        if percent > 100.00:
            percent = 99
        return Response({"result": f"{int(percent)}%"})
        
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