from rest_framework import serializers

from .models import *
from src.users.serializers import UserSerializer


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Projects
        fields = '__all__'


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class PositionsDetailSerializer(serializers.ModelSerializer):
    project = ProjectsDetailSerializer()

    class Meta:
        model = Positions
        fields = '__all__'


class ProjectParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectParticipants
        fields = '__all__'


class ProjectParticipantsDetailSerializer(serializers.ModelSerializer):
    project = ProjectsDetailSerializer()
    user = UserSerializer()
    position = PositionsDetailSerializer()

    class Meta:
        model = ProjectParticipants
        fields = '__all__'
