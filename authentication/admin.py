from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

#importing User Model
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(DjangoUserAdmin) :
    
    """
        Define admin model for custom User model with no email field.
    """

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','mobile_number', 'bio', 'location')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'mobile_number', 'bio', 'location'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'mobile_number', 'bio', 'location')
    search_fields = ('email', 'first_name', 'last_name', 'mobile_number', 'location')
    ordering = ('email',)

