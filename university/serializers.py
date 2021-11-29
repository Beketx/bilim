from rest_framework import serializers
from school.models import SubjectFirst

from university.models import Specialty, Stuff, University, Faculty, GrantPoint


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ['id', 'title', 'address', 'image']


class SpecialtyDetailedSerializer(serializers.ModelSerializer):
    faculty = serializers.SerializerMethodField()
    grant_point = serializers.SerializerMethodField()
    subject_one = serializers.SerializerMethodField()
    subject_two = serializers.SerializerMethodField()
    stuff = serializers.SerializerMethodField()

    class Meta:
        model = Specialty
        fields = ['id', 'title', 'faculty', 'grant_point',
                   'subject_one', 'subject_two', 'stuff']

    def get_faculty(self, obj):
        return obj.faculty.title

    def get_grant_point(self, obj):
        grant = GrantPoint.objects.get(specialty=obj)
        return grant.point
    
    def get_subject_one(self, obj):
        subject_one = GrantPoint.objects.get(specialty=obj)
        return subject_one.subject_first.title
    
    def get_subject_two(self, obj):
        subject_two = GrantPoint.objects.get(specialty=obj)
        return subject_two.subject_second.title
    
    def get_stuff(self, obj):
        stuff = Stuff.objects.get(faculty=obj.faculty)
        return stuff.bio


class SpecialtySerializer(serializers.ModelSerializer):
    faculty = serializers.SerializerMethodField()
    grant_point = serializers.SerializerMethodField()
    class Meta:
        model = Specialty
        fields = ['id', 'title', 'faculty', 'grant_point']

    def get_faculty(self, obj):
        return obj.faculty.title

    def get_grant_point(self, obj):
        grant = GrantPoint.objects.get(specialty=obj)
        return grant.point

class UniversityDetailedSerializer(serializers.ModelSerializer):
    specialty = serializers.SerializerMethodField('get_specialty')
    city = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ['id', 'title', 'city', 'image', 'specialty']

    def get_city(self, obj):
        return obj.city.title

    def get_specialty(self, obj):
        faculties = Faculty.objects.filter(university=obj).values_list('id', flat=True)
        specialties = Specialty.objects.filter(faculty__in=faculties)
        serializer = SpecialtySerializer(specialties, many=True)
        return serializer.data

class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ['id', 'title', 'university__title']



class ReadSpecialtySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()    


class DetailedFacultySerializer(serializers.ModelSerializer):

    specialty = SpecialtySerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = ['id', 'title', 'specialty']

class DetailedUniversitySerializer(serializers.ModelSerializer):
    pass
    