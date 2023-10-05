from django.contrib import admin
from django.contrib.admin import register
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from demo.models import UserModel


@register(UserModel)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'registered_time']
    # change_password_form = AdminPasswordChangeForm

    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    #     (_('Permissions'), {
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password'),
    #     }),
    # )
