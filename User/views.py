from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from User.models import User
import jwt , datetime

# Create your views here.
class Register(APIView):
    def post(self, request):
        if  User.objects.filter(email=request.data['email']).exists():
           raise AuthenticationFailed("Account Already Exist")
        else:
            serialzer = UserSerializer(data=request.data)
            serialzer.is_valid(raise_exception=True)
            serialzer.save()
        
        return Response(serialzer.data)
class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not Found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data = {
            'jwt':token,
            "user_info":{
                "user_id":user.id,
                "first_name":user.first_name,
                "last_name":user.last_name,
                "email":user.email,
                "phone":user.phone
            }
        }
        return response
    
class Logout(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':"logged out "
        }
        return response
