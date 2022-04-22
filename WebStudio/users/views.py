from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from users.models import *
from users.serializers import CustomUserSerializer


class UsersListCreateView(ListAPIView, CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUsers.objects.all()


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUsers.objects.all()


class UsersProjectListView(RetrieveUpdateDestroyAPIView):
    # serializer_class = CustomUserSerializer
    # queryset = CustomUsers.objects.all()
    ...
