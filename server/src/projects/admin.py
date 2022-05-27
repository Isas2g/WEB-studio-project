from django.contrib import admin
from .models import *


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'creator')
    list_display_links = ('id',)


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project', 'color')
    list_display_links = ('id',)


@admin.register(ProjectParticipants)
class ProjectParticipantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'position')
    list_display_links = ('id',)
