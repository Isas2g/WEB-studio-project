from django.contrib import admin
from .models import *


@admin.register(Boards)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'created_at', 'ended_at')
    list_display_links = ('id',)


@admin.register(TaskTags)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'color')
    list_display_links = ('id',)


@admin.register(Tasks)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'board', 'created_at', 'is_done', 'executor', 'done_at', 'author', 'tag')
    list_display_links = ('id',)


@admin.register(BoardColumns)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'board', 'title', 'creator')
    list_display_links = ('id',)


@admin.register(BoardTasks)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'board', 'task', 'column')
    list_display_links = ('id',)


@admin.register(TaskComment)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'author', 'updated_at', 'is_reply', 'reply_comment')
    list_display_links = ('id',)
