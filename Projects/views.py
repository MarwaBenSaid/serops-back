from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projects
from rest_framework import  status
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import generics

@permission_classes([IsAuthenticated])
class RetrieveAllView(generics.ListAPIView):
    def get(self,request):
        user_projects = Projects.objects.all()
        serializer = ProjectSerializer(user_projects,many=True)
        return Response(serializer.data)
        

@permission_classes([IsAuthenticated])    
class RetrieveView(APIView):
    def get(self,request,id):
        project = Projects.objects.get(id=id)
        serializer = ProjectSerializer(project)
        lookup_field = 'id'
        return Response({"project": serializer.data}, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class CreateView(APIView):
    def post(self, request):
        #return Response([request.data.get('user'),request.data.get('organisation')])
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
        return Response({"project_info":serializer.data}, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class UpdateView(APIView):
    def post(self, request,id):
        if request.data.get('name') is None:
            return Response({"error":"invalid data"})
        if request.data.get('type') is None:
            return Response({"error":"invalid data"})
        project = Projects.objects.get(id=id)
        serializer = ProjectSerializer(project,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"project":serializer.data})
        else:
            return Response({"error":"invalid data"})

@permission_classes([IsAuthenticated])
class DeleteView(APIView):
    def delete(self,request,id):
        project = Projects.objects.get(id=id)
        if project is None:
            return Response({"error":"project not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            project.delete()
            return Response({"success":"project deleted"})