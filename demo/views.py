from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from lib.throttle import LoginThrottle1, LoginThrottle2
from .models import UserModel, LoginModel
from .serializers import UserSerializer, LoginSerializer
from django.conf import settings
from django.utils import timezone
from rest_framework.response import Response


class UserListAPI(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class ProfileAPI(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class LoginAPI(ListCreateAPIView):
    queryset = LoginModel.objects.all()
    serializer_class = LoginSerializer


class ApiToken(TokenObtainPairView):
    throttle_classes = [LoginThrottle1, LoginThrottle2]
