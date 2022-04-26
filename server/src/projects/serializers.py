from rest_framework import serializers

from .models import *


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsDetailSerializer(serializers.ModelSerializer):
    # creator_id = CustomUsersDetailSerializer()

    class Meta:
        model = Projects
        fields = '__all__'


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class PositionsDetailSerializer(serializers.ModelSerializer):
    project_id = ProjectsDetailSerializer()

    class Meta:
        model = Positions
        fields = '__all__'


class ProjectParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectParticipants
        fields = '__all__'


class ProjectParticipantsDetailSerializer(serializers.ModelSerializer):
    project_id = ProjectsDetailSerializer()
    # user_id = CustomUsersDetailSerializer()
    position_id = PositionsDetailSerializer()

    class Meta:
        model = ProjectParticipants
        fields = '__all__'
