from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from src.users.models import CustomUsers


class CustomUserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = CustomUsers
        fields = ('id', 'username', 'password', 'email')

    def create(self, validated_data):
        user = CustomUsers.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],

        )
        return user
