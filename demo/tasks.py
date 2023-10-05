import smtplib
from email.message import EmailMessage
import random

from celery import shared_task
# from django.contrib.auth.models import User

from demo.local_config import HOST_USER, HOST_PASSWORD
from demo.models import UserModel


@shared_task(name='send_email')
def send_email(email_address, code):
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = HOST_USER
    EMAIL_HOST_PASSWORD = HOST_PASSWORD
    HOST_PORT_TLS = 587
    HOST_PORT_SSL = 465
    contacts = [email_address, ]

    msg = EmailMessage()
    msg['Subject'] = "djangoOTP"
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = ', '.join(contacts)

    msg.set_content(f"code: {code}")
    with smtplib.SMTP_SSL(EMAIL_HOST, HOST_PORT_SSL) as gmail:
        gmail.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        gmail.send_message(msg)
        reset_password.apply_async([email_address, ], countdown=300)


@shared_task(name='reset_password')
def reset_password(email):
    user = UserModel.objects.filter(email=email).first()
    if user:
        password = UserModel.objects.make_random_password(length=16)
        user.set_password(password)
        user.save()
