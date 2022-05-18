from django.urls import path

from src.users.endpoint import auth_views
from src.users.endpoint.views import *

urlpatterns = [
    path('auth/', auth_views.google_login),
    path('auth/google/', auth_views.google_auth_),

    path('', UsersListCreateView.as_view()),
    path('<int:id>/', UsersRetrieveUpdateDestroyView.as_view()),

    # path('{id}/projects/', UsersRetrieveUpdateDestroyView.as_view()),

    path('contacts/', UserContactCreateView.as_view()),
    path('contacts/<int:id>/', UserContactRetrieveUpdateDestroyView.as_view()),
    path('<int:user_id>/contacts', UserContactListView.as_view()),
]
