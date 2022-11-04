from django.urls import path

from .views import *

urlpatterns = [
    path('', ProjectsListCreateView.as_view()),
    path('<int:pk>/files', ProjectsFilesView.as_view()),
    path('<int:pk>/', ProjectsView.as_view()),
    path('positions/', PositionsListCreateView.as_view()),
    path('positions/<int:pk>/', PositionsView.as_view()),
    path('participants/', ProjectParticipantsCreateView.as_view()),
    path('participants/<int:pk>/', ProjectParticipantsView.as_view()),
]
