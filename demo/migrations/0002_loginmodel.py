# Generated by Django 3.2 on 2023-10-05 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator()])),
                ('login_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]