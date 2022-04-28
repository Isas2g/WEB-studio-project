from django.contrib import admin
from .models import *


@admin.register(User)
class CustomUsersAdmin(admin.ModelAdmin):
    fields = ['role']
    list_display = ('id', 'username', 'email', 'join_date', 'disabled_at')
    list_display_links = ('username',)


@admin.register(UserContact)
class UserContactsAdmin(admin.ModelAdmin):
    fields = ['user']
    list_display = ('id', 'title', 'contact')
    list_display_links = ('id',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'access_level')
    list_display_links = ('id',)
