from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('fullname', 'badge_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ['email', 'fullname', 'badge_number', 'is_superuser']
    search_fields = ['email', 'fullname', 'badge_number']
    ordering = ['id']
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('email', 'fullname', 'password1', 'password2')}),)
    readonly_fields = ['badge_number']
