from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Web Studio",
        default_version='v1',
        description="Web Studio",
        contact=openapi.Contact(url="https://vk.com/mihey_5389"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('users/', include('src.users.urls')),
    path('boards/', include('src.boards.urls')),
    path('projects/', include('src.projects.urls')),
]

