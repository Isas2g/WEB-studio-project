from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class ProjectsListCreateView(APIView):
    def post(self, request):
        project = ProjectsSerializer(data=request.data)
        if project.is_valid():
            project.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get(self, request):
        project = Projects.objects
        serializer = ProjectsSerializer(project, many=True)
        return Response(serializer.data)


class ProjectsView(APIView):
    def get(self, request, pk):
        project = Projects.objects.get(id=pk)
        serializer = ProjectsDetailSerializer(project)
        return Response(serializer.data)

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


class PositionsListCreateView(APIView):
    def get(self, request):
        position = Positions.objects
        serializer = PositionsSerializer(position, many=True)
        return Response(serializer.data)

    def post(self, request):
        position = PositionsSerializer(data=request.data)
        if position.is_valid():
            position.save()
            return Response(status=201)
        else:
            return Response(status=400)


class PositionsView(APIView):
    def get(self, request, pk):
        position = Positions.objects.get(id=pk)
        serializer = PositionsDetailSerializer(position)
        return Response(serializer.data)

    def patch(self, request, pk):
        position = Positions.objects.get(id=pk)
        serializer = PositionsSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(PositionsDetailSerializer(Positions.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        position = Positions.objects.get(id=pk)
        position.delete()
        return Response(status=201)


class ProjectParticipantsCreateView(APIView):

    def post(self, request):
        project_participants = ProjectParticipantsSerializer(data=request.data)
        if project_participants.is_valid():
            project_participants.save()
            return Response(status=201)
        else:
            return Response(status=400)


class ProjectParticipantsView(APIView):
    def get(self, request, pk):
        project_participants = ProjectParticipants.objects.get(id=pk)
        serializer = ProjectParticipantsDetailSerializer(project_participants)
        return Response(serializer.data)

    def patch(self, request, pk):
        project_participants = ProjectParticipants.objects.get(id=pk)
        serializer = ProjectParticipantsSerializer(project_participants, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ProjectParticipants(ProjectParticipants.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        project_participants = ProjectParticipants.objects.get(id=pk)
        project_participants.delete()
        return Response(status=201)
