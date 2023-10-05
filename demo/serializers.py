from datetime import datetime, timedelta
import random
from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UserModel, LoginModel
from .tasks import send_email
from django.core.validators import validate_email as validate_email_address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        otp = random.randint(100000, 999999)
        user = UserModel.objects.create(
            email=validated_data['email'],
            is_active=True,
        )
        user.set_password(str(otp))
        user.save()
        send_email.delay(email_address=user.email, code=otp)
        return user

    def validate_email(self, attr):
        user = UserModel.objects.filter(email=attr)
        if user:
            raise serializers.ValidationError('This email is already registered!')
        return attr


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ('id', 'email')
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        user = UserModel.objects.filter(email=email).first()
        if user:
            otp = random.randint(100000, 999999)
            user.set_password(str(otp))
            user.save()
            send_email.delay(email_address=email, code=otp)
        login = LoginModel.objects.create(email=email)
        return login

    def validate_email(self, attr):
        user = UserModel.objects.filter(email=attr)
        if not user:
            raise serializers.ValidationError('This email is not registered!')
        validate_email_address(attr)
        return attr
