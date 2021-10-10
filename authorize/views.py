from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from django.core.cache import cache

from authorize.models import User, UserActivation
from authorize.serializers import LoginWriteSerializer, UserResponseSerializer, ForgetPasswordWriteSerializer, \
    ActivateSerializer, RegisterSerializer
from authorize.services.auth_token import delete_token
from authorize.services.auth_user import authenticate_user, get_client_ip, user_email_existence, activate_user
from authorize.services.user_mail import send_renew_link_to_mail


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def login(self, request, **kwargs):
        """User authorization"""
        serializer = LoginWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ip = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT')
        user = authenticate_user(email=serializer.validated_data.get('email').lower(),
                                 password=serializer.validated_data.get('password'),
                                 ip=ip,
                                 user_agent=user_agent)

        return Response(UserResponseSerializer(user).data)

    @action(detail=False, methods=['post'], permission_classes=(IsAuthenticated,))
    def logout(self, request, **kwargs):
        """Makes a logout and deletes the token"""
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            delete_token(request.user, token, request.data.get('all') is not None)
        except:
            pass
        return Response()

    @action(detail=False, methods=['post'])
    def forget_password(self, request, **kwargs):
        """Forgot your password? Sends a confirmation email to the user"""
        serializer = ForgetPasswordWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        code = serializer.validated_data.get('code')
        if cache.get('email_time_' + str(email)) is not None:
            raise ValidationError({'status': 0, 'detail': 'Confirmation has already been sent to your email!'})

        user = user_email_existence(email=email)
        send_renew_link_to_mail(user, email, code)
        return Response({'status': 1, 'detail': 'Successfully sent to your email!'})

    @action(detail=False, methods=['get'])
    def activate(self, request, **kwargs):
        """Activating an account with a code from your email"""
        serializer = ActivateSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        activate_user(serializer.validated_data.get('code'))

        return Response()

    @action(detail=False, methods=['post'])
    def register(self, request, **kwargs):
        """Account registration"""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response()

    @action(detail=False, methods=['get'], permission_classes=(IsAuthenticated,))
    def get_users(self, request, *args, **kwargs):
        """Get statistics of activated and non-activated users"""
        data = {
            "name": "Test"
        }
        return Response(data)

















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
