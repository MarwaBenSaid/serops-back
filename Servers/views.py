from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Servers
from rest_framework import  status
from .serializers import ServerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import generics

@permission_classes([IsAuthenticated])
class RetrieveAllView(generics.ListAPIView):
    def get(self,request):
        servers = Servers.objects.all()
        serializer = ServerSerializer(servers,many=True)
        return Response(serializer.data)
        

@permission_classes([IsAuthenticated])    
class RetrieveView(APIView):
    def get(self,request,id):
        project = Servers.objects.get(id=id)
        serializer = ServerSerializer(project)
        lookup_field = 'id'
        return Response({"server": serializer.data}, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class CreateView(APIView):
    def post(self, request):
        serializer = ServerSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
        return Response({"server_info":serializer.data}, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class UpdateView(APIView):
    def post(self, request,id):
        if request.data.get('name') is None:
            return Response({"error":"invalid data"})
        if request.data.get('ip') is None:
            return Response({"error":"invalid data"})
        if request.data.get('password') is None:
            return Response({"error":"invalid data"})
        if request.data.get('key') is None:
            return Response({"error":"invalid data"})
        server = Servers.objects.get(id=id)
        serializer = ServerSerializer(server,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"server":serializer.data})
        else:
            return Response({"error":"invalid data"})

@permission_classes([IsAuthenticated])
class DeleteView(APIView):
    def delete(self,request,id):
        server = Servers.objects.get(id=id)
        if server is None:
            return Response({"error":"server not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            server.delete()
            return Response({"success":"server deleted"})