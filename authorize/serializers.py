from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)