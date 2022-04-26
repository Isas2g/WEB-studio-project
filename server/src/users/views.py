from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from src.users.models import *
from src.users.serializers import UserSerializer


class UsersListCreateView(ListAPIView, CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersProjectListView(RetrieveUpdateDestroyAPIView):
    # serializer_class = CustomUserSerializer
    # queryset = CustomUsers.objects.all()
    ...
