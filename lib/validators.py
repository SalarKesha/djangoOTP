from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.conf import settings


class PasswordValidator(MinimumLengthValidator):
    def __init__(self):
        super().__init__(min_length=settings.MIN_PASSWORD_LENGTH)
