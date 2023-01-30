from django.urls import path

from .views import *

urlpatterns = [
    path('', BoardsCreateView.as_view()),
    path('<int:pk>/', BoardsView.as_view()),
    path('tasks/', TasksCreateView.as_view()),
    path('tasks/<int:pk>/', TasksView.as_view()),
    path('board_columns/', BoardColumnsCreateView.as_view()),
    path('board_columns/<int:pk>/', BoardColumnsView.as_view()),
    path('task_tags/', TaskTagsCreateView.as_view()),
    path('task_tags/<int:pk>/', TaskTagsView.as_view()),
    path('board_tasks/', BoardTasksCreateView.as_view()),
    path('board_tasks/<int:pk>/', BoardTasksView.as_view()),
    path('task_comment/', TaskCommentCreateView.as_view()),
    path('task_comment/<int:pk>/', TaskCommentView.as_view()),
]
