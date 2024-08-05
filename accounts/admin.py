from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['full_name', 'email', 'is_admin', 'last_login']
    list_filter = ['is_admin']

    fieldsets = [
        (
            None, {'fields': ['full_name', 'email', 'password', 'last_login']}
        ),
        (
            "Permissions", {'fields': ['is_admin', 'is_active', 'is_superuser', 'groups', 'user_permissions']}
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                'fields': ['full_name', 'email', 'password1', 'password2']
            }
        ),
    ]

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ['groups', 'user_permissions']
    readonly_fields = ['last_login']



admin.site.register(User, UserAdmin)
