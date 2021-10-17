from rest_framework import serializers

from university.models import University, Faculty


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ['title', 'address']


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ['title', 'university__title']
