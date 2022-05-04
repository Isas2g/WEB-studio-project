from django.urls import path

from .views import *

urlpatterns = [
    path('', BoardsCreateView.as_view()),
    path('{pk}/', BoardsView.as_view()),
    path('tasks/', TasksCreateView.as_view()),
    path('tasks/{pk}/', TasksView.as_view()),
    path('board_columns/', BoardColumnsCreateView.as_view()),
    path('board_columns/{pk}/', BoardColumnsView.as_view()),
    path('task_tags/', TaskTagsCreateView.as_view()),
    path('task_tags/{pk}/', TaskTagsView.as_view()),
    path('board_tasks/', BoardTasksCreateView.as_view()),
    path('board_tasks/{pk}/', BoardTasksView.as_view()),
    path('task_comment/', TaskCommentCreateView.as_view()),
    path('task_comment/{pk}/', TaskCommentView.as_view()),
]
