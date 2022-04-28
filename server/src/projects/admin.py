from django.contrib import admin
from .models import *


@admin.register(Projects)
class CustomProjectsAdmin(admin.ModelAdmin):
    fields = ['creator']
    list_display = ('id', 'title', 'created_at', 'closed_at', 'description', 'icon_url')
    list_display_links = ('id',)


@admin.register(Positions)
class CustomPositionsAdmin(admin.ModelAdmin):
    fields = ['project']
    list_display = ('id', 'name', 'color')
    list_display_links = ('id',)


@admin.register(ProjectParticipants)
class CustomProjectParticipantsAdmin(admin.ModelAdmin):
    fields = ['project', 'user', 'position']
    list_display = ('id', 'invited_at', 'kicked_at')
    list_display_links = ('id',)
