from django.contrib import admin
from .models import *


@admin.register(Boards)
class CustomBoardsAdmin(admin.ModelAdmin):
    fields = ['project']
    list_display = ('id', 'title', 'created_at', 'ended_at')
    list_display_links = ('id',)


@admin.register(TaskTags)
class CustomTaskTagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'color')
    list_display_links = ('id',)


@admin.register(Tasks)
class CustomTasksAdmin(admin.ModelAdmin):
    fields = ['board', 'executor', 'author', 'tag']
    list_display = ('id', 'title', 'description', 'created_at', 'is_done', 'done_at')
    list_display_links = ('id',)


@admin.register(BoardColumns)
class CustomBoardColumnsAdmin(admin.ModelAdmin):
    fields = ['board', 'creator']
    list_display = ('id', 'title')
    list_display_links = ('id',)


@admin.register(BoardTasks)
class CustomBoardTasksAdmin(admin.ModelAdmin):
    fields = ['board', 'task', 'column']
    list_display = ('id',)
    list_display_links = ('id',)


@admin.register(TaskComment)
class CustomTaskCommentAdmin(admin.ModelAdmin):
    fields = ['author', 'reply_comment']
    list_display = ('id', 'content', 'created_at', 'updated_at', 'is_reply')
    list_display_links = ('id',)
