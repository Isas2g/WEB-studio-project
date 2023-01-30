from loguru import logger
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, \
    get_object_or_404

from src.users.models import *
from src.users.serializers import UserSerializer, UserContactSerializer


class UsersListCreateView(ListAPIView, CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserContactCreateView(CreateAPIView):
    serializer_class = UserContactSerializer
    queryset = UserContact.objects.all()


class UserContactListView(ListAPIView):
    lookup_field = 'user_id'
    serializer_class = UserContactSerializer
    queryset = UserContact.objects.all()

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserContact.objects.filter(user_id=user_id)


class UserContactRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserContactSerializer
    queryset = UserContact.objects.all()


class UsersProjectListView(RetrieveUpdateDestroyAPIView):
    # serializer_class = CustomUserSerializer
    # queryset = CustomUsers.objects.all()
    ...
