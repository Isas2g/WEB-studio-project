from django.urls import path

from .views import *

urlpatterns = [
    path('', BoardsCreateView.as_view()),
    path('{pk}/', BoardsView.as_view()),
    path('tasks/', TasksCreateView.as_view()),
    path('tasks/{pk}/', TasksView.as_view()),
]
