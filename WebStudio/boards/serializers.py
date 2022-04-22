from rest_framework import serializers

from .models import *


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = '__all__'


class BoardsDetailSerializer(serializers.ModelSerializer):
    # project_id = ProjectsDetailSerializer()

    class Meta:
        model = Boards
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TasksDetailSerializer(serializers.ModelSerializer):
    board_id = BoardsDetailSerializer()
    # executor_id = ExecutorDetailSerializer()
    # author_id = AuthorDetailSerializer()
    # tag_id = TagDetailSerializer()

    class Meta:
        model = Tasks
        fields = '__all__'


class BoardColumnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardColumns
        fields = '__all__'


class BoardColumnsDetailSerializer(serializers.ModelSerializer):
    board_id = BoardsDetailSerializer()
    # creator_id = CustomUsersDetailSerializer()

    class Meta:
        model = BoardColumns
        fields = '__all__'


class TaskTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskTags
        fields = '__all__'


class BoardTasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardTasks
        fields = '__all__'


class BoardTasksDetailSerializer(serializers.ModelSerializer):
    board_id = BoardsDetailSerializer()
    task_id = TasksDetailSerializer()
    column_id = BoardColumnsDetailSerializer()

    class Meta:
        model = BoardTasks
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'


class TaskCommentDetailSerializer(serializers.ModelSerializer):
    # author_id = CustomUsersDetailSerializer()
    # reply_comment_id =

    class Meta:
        model = TaskComment
        fields = '__all__'