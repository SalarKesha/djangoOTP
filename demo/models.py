from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator, validate_email


# PHONE_REGEX = RegexValidator(regex=r"^\d{10}", message='phone number must be 10 digits only!')


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email address is required!')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    # phone_number = models.CharField(unique=True, max_length=10, null=False, blank=False, validators=[PHONE_REGEX, ])
    email = models.EmailField(unique=True, max_length=50, blank=True, null=True, validators=[validate_email])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    registered_time = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    # default_manager = models.Manager()
    objects = UserManager()

    def __str__(self):
        return self.email


class LoginModel(models.Model):
    email = models.EmailField(max_length=50, validators=[validate_email])
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

