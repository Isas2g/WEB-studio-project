from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class BoardsCreateView(APIView):

    def post(self, request):
        board = BoardsSerializer(data=request.data)
        if board.is_valid():
            board.save()
            return Response(status=201)
        else:
            return Response(status=400)


class BoardsView(APIView):

    def get(self, request, pk):
        board = Boards.objects.get(id=pk)
        serializer = BoardsDetailSerializer(board)
        return Response(serializer.data)

    def patch(self, request, pk):
        board = Boards.objects.get(id=pk)
        serializer = BoardsSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(BoardsDetailSerializer(Boards.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        board = Boards.objects.get(id=pk)
        board.delete()
        return Response(status=201)


class TasksCreateView(APIView):

    def post(self, request):
        task = TasksSerializer(data=request.data)
        if task.is_valid():
            task.save()
            return Response(status=201)
        else:
            return Response(status=400)


class TasksView(APIView):

    def get(self, request, pk):
        task = Tasks.objects.get(id=pk)
        serializer = TasksDetailSerializer(task)
        return Response(serializer.data)

    def patch(self, request, pk):
        task = Tasks.objects.get(id=pk)
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(TasksDetailSerializer(Tasks.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        task = Tasks.objects.get(id=pk)
        task.delete()
        return Response(status=201)


class BoardColumnsView(APIView):

    def get(self, request, pk):
        board_columns = BoardColumns.objects.get(id=pk)
        serializer = BoardColumnsDetailSerializer(board_columns)
        return Response(serializer.data)

    def post(self, request):
        board_columns = BoardColumnsSerializer(data=request.data)
        if board_columns.is_valid():
            board_columns.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        board_columns = BoardColumns.objects.get(id=pk)
        serializer = BoardColumnsSerializer(board_columns, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(BoardColumnsDetailSerializer(BoardColumns.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        board_columns = BoardColumns.objects.get(id=pk)
        board_columns.delete()
        return Response(status=201)


class TaskTagsView(APIView):

    def get(self, request, pk):
        task_tags = TaskTags.objects.get(id=pk)
        serializer = TaskTagsSerializer(task_tags)
        return Response(serializer.data)

    def post(self, request):
        task_tags = TaskTagsSerializer(data=request.data)
        if task_tags.is_valid():
            task_tags.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        task_tags = TaskTags.objects.get(id=pk)
        serializer = TaskTagsSerializer(task_tags, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        task_tags = TaskTags.objects.get(id=pk)
        task_tags.delete()
        return Response(status=201)


class BoardTasksView(APIView):

    def get(self, request, pk):
        board_task = BoardTasks.objects.get(id=pk)
        serializer = BoardTasksDetailSerializer(board_task)
        return Response(serializer.data)

    def post(self, request):
        board_task = BoardTasksSerializer(data=request.data)
        if board_task.is_valid():
            board_task.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        board_task = BoardTasks.objects.get(id=pk)
        serializer = BoardTasksSerializer(board_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(BoardTasksDetailSerializer(BoardTasks.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        board_task = BoardTasks.objects.get(id=pk)
        board_task.delete()
        return Response(status=201)


class TaskCommentView(APIView):

    def get(self, request, pk):
        task_comment = TaskComment.objects.get(id=pk)
        serializer = TaskCommentDetailSerializer(task_comment)
        return Response(serializer.data)

    def post(self, request):
        task_comment = TaskCommentSerializer(data=request.data)
        if task_comment.is_valid():
            task_comment.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        task_comment = TaskComment.objects.get(id=pk)
        serializer = TaskCommentSerializer(task_comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(TaskCommentDetailSerializer(TaskComment.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        task_comment = TaskComment.objects.get(id=pk)
        task_comment.delete()
        return Response(status=201)
