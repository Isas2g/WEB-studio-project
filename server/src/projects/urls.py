from django.urls import path

from .views import *

urlpatterns = [
    path('', ProjectsListCreateView.as_view()),
    path('{pk}/', ProjectsView.as_view()),
    path('positions/', PositionsListCreateView.as_view()),
    path('positions/{pk}/', PositionsView.as_view()),
    path('participants/', ProjectParticipantsCreateView.as_view()),
    path('participants/{pk}/', ProjectParticipantsView.as_view()),
]
