from django.contrib import admin
from .models import *


@admin.register(CustomUsers)
class CustomUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'join_date')
    list_display_links = ('email',)


@admin.register(UserContacts)
class UserContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'contact')