from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class ProjectsView(APIView):
    def get(self, request, pk):
        project = Projects.objects.get(id=pk)
        serializer = ProjectsDetailSerializer(project)
        return Response(serializer.data)

    def post(self, request):
        project = ProjectsSerializer(data=request.data)
        if project.is_valid():
            project.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        project = Projects.objects.get(id=pk)
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ProjectsDetailSerializer(Projects.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        project = Projects.objects.get(id=pk)
        project.delete()
        return Response(status=201)


class PositionsView(APIView):
    def get(self, request, pk):
        board = Positions.objects.get(id=pk)
        serializer = PositionsDetailSerializer(board)
        return Response(serializer.data)

    def post(self, request):
        board = PositionsSerializer(data=request.data)
        if board.is_valid():
            board.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        board = Positions.objects.get(id=pk)
        serializer = PositionsSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(PositionsDetailSerializer(Positions.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        board = Positions.objects.get(id=pk)
        board.delete()
        return Response(status=201)


class ProjectParticipantsView(APIView):
    def get(self, request, pk):
        board = ProjectParticipants.objects.get(id=pk)
        serializer = ProjectParticipantsDetailSerializer(board)
        return Response(serializer.data)

    def post(self, request):
        board = ProjectParticipantsSerializer(data=request.data)
        if board.is_valid():
            board.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def patch(self, request, pk):
        board = ProjectParticipants.objects.get(id=pk)
        serializer = ProjectParticipantsSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ProjectParticipants(ProjectParticipants.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        board = ProjectParticipants.objects.get(id=pk)
        board.delete()
        return Response(status=201)
