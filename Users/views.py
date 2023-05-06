from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from Organisations.models import  Organisations
from Organisations.serializers import  OrganisationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import  status,authentication
from django.contrib import auth
from rest_framework.response import Response


@permission_classes([AllowAny])
class RegisterView(APIView):
    def post(self, request):
        #return Response([request.data.get('user'),request.data.get('organisation')])
        serializer = UserSerializer(data=request.data.get('user'))
        orgnisation_serializer = OrganisationSerializer(data=request.data.get('organisation'))
        if serializer.is_valid():
            if orgnisation_serializer.is_valid():
                user_orgnisation =orgnisation_serializer.save()
                user = serializer.save()
                user.organisation_id=user_orgnisation.id 
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(orgnisation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class LoginView(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user is not None:
            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password!')
            else:
                if user.status=="suspended":
                    return Response({'detail': 'Account is suspended'}, status=status.HTTP_401_UNAUTHORIZED)
                elif user.status == "disabled":
                    return Response({'detail': 'Account is disabled'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    Token.objects.filter(user=user).delete()
                    token = Token.objects.create(user=user)
                    auth.login(request, user)
                    return Response({
                        'token': token.key,
                        'user': UserSerializer(user).data
                        })
        else:
            return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def post(self,request):
        token = request.auth
        token.delete()
        auth.logout(request)
        return Response({
            "message": "You have successfully logged out.",
        }, status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])
class ActiveView(APIView):
    def get(self,request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response({ "user":serializer.data },status=status.HTTP_200_OK)