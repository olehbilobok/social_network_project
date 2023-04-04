from django.contrib import admin
from django.contrib.auth.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'last_login',
                    'is_active', 'is_staff', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
