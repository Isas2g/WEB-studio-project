from django.urls import path, include

urlpatterns = [
    path('users/', include('src.users.urls')),
    path('boards/', include('src.boards.urls')),
    path('projects/', include('src.projects.urls')),
]
