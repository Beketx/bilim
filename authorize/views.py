from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from authorize.serializers import TestSerializer


class TestView(APIView):

    def get(self, request):
        data = {
            "name": "Test"
        }
        return Response(data)


class TestViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def testsets(self, request):
        data = request.data
        serializer = TestSerializer(data).data

        return Response(serializer)
