from rest_framework import serializers

from university.models import Specialty, University, Faculty


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ['id', 'title', 'address', 'image']


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ['id', 'title', 'university__title']


class SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialty
        fields = ['id', 'title', 'faculty__title']


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
    