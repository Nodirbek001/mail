from django.contrib import admin

from apps.users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'phone_number', 'email')
