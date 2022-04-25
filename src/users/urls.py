from django.urls import path

from .views import *

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/{id}/', UsersRetrieveUpdateDestroyView.as_view()),
    path('/{id}/projects/', UsersRetrieveUpdateDestroyView.as_view()),
]
