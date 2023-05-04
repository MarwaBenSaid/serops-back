from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from rest_framework import  status
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import generics

@permission_classes([IsAuthenticated])
class RetrieveAllView(generics.ListAPIView):
    def get(self,request):
        user_projects = Project.objects.all()
        serializer = ProjectSerializer(user_projects,many=True)
        return Response(serializer.data)
        

@permission_classes([IsAuthenticated])    
class RetrieveView(APIView):
    def get(self,request,id):
        project = Project.objects.get(id=id)
        serializer = ProjectSerializer(project)
        lookup_field = 'id'
        return Response({"project": serializer.data}, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class CreateView(APIView):
    def post(self, request):
        #return Response([request.data.get('user'),request.data.get('organisation')])
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
           project= serializer.save()
        return Response({"project_info":project.name}, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class UpdateView(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

@permission_classes([IsAuthenticated])
class DeleteView(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'