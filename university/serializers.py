from rest_framework import serializers

from university.models import Specialty, University, Faculty


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ['id', 'title', 'address', 'image']


class SpecialtySerializer(serializers.ModelSerializer):
    faculty = serializers.SerializerMethodField()
    # grant_point = serializers.SerializerMethodField()
    class Meta:
        model = Specialty
        fields = ['id', 'title', 'faculty']

    def get_faculty(self, obj):
        return obj.faculty.title

    # def get_grant_point(self, obj):
    #     grant = GrantPoint.objects.get(specialty=obj).values('point')
    #     return grant

class UniversityDetailedSerializer(serializers.ModelSerializer):
    specialty = serializers.SerializerMethodField('get_specialty')

    class Meta:
        model = University
        fields = ['id', 'title', 'address', 'image', 'specialty']

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
    