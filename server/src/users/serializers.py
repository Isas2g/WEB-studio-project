from django.db.models import Model
from loguru import logger
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import CharField, EmailField, ModelSerializer, Serializer

from src.users.models import User, UserContact, UserRole


class UserRoleSerializer(ModelSerializer):
    class Meta:
        model = UserRole
        fields = ('id', 'title', 'access_level')


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    role = UserRoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'role', 'position', 'avatar')

    def create(self, validated_data):
        logger.debug(validated_data)
        user = User.objects.create_user(
            **validated_data
        )
        return user


class UserContactSerializer(ModelSerializer):
    class Meta:
        model = UserContact
        fields = ('id', 'title', 'contact')


class GoogleAuthSerializer(Serializer):
    email = EmailField()
    token = CharField()
