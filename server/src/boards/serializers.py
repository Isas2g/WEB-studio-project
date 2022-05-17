from rest_framework import serializers

from .models import *
from src.projects.serializers import ProjectsDetailSerializer
from src.users.serializers import UserSerializer


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = '__all__'


class BoardsDetailSerializer(serializers.ModelSerializer):
    project = ProjectsDetailSerializer()

    class Meta:
        model = Boards
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTags
        fields = '__all__'


class TasksDetailSerializer(serializers.ModelSerializer):
    board = BoardsDetailSerializer()
    executor = UserSerializer()
    author = UserSerializer()
    tag = TaskTagsSerializer()

    class Meta:
        model = Tasks
        fields = '__all__'


class BoardColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardColumns
        fields = '__all__'


class BoardColumnsDetailSerializer(serializers.ModelSerializer):
    board = BoardsDetailSerializer()
    creator = UserSerializer()

    class Meta:
        model = BoardColumns
        fields = '__all__'


class BoardTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardTasks
        fields = '__all__'


class BoardTasksDetailSerializer(serializers.ModelSerializer):
    board = BoardsDetailSerializer()
    task = TasksDetailSerializer()
    column = BoardColumnsDetailSerializer()

    class Meta:
        model = BoardTasks
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'


class TaskCommentDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    reply_comment = TaskCommentSerializer()

    class Meta:
        model = TaskComment
        fields = '__all__'
