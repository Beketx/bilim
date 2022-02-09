from rest_framework import serializers
from authorize.serializers import ProfileSerializer

from university.serializers import FacultySerializer, SpecialtyWriteSerializer, UniversitySerializer
from .models import Car, Computer, Mouse

class CarSerializers(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

class ComputerSerializers(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    user = ProfileSerializer(read_only=True)
    faculty = FacultySerializer(read_only=True)
    specialty = SpecialtyWriteSerializer(read_only=True)

    class Meta:
        model = Computer
        fields = '__all__'

class MouseSerializers(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)


    class Meta:
        model = Mouse
        fields = '__all__'

