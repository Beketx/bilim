from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from authorize.models import User, UserActivation
from authorize.serializers import LoginWriteSerializer


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def login(self, request, **kwargs):
        """User authorization"""
        serializer = LoginWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ip = get_client_ip(request)














##-------------------------------------------------------------------------
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
