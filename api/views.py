from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.models import *
from .serializers import CustomUserSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.forms import *
from rest_framework import generics

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['is_superuser'] = user.is_superuser
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['is_superuser'] = user.is_superuser
        # ...

        return token

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        '/api/usertable/'  
        '/api/add/',
        '/api/usertoken/',
        '/api/usertoken/refresh/', 
        '/api/users/',
        '/api/cred/<int:pk>',
    ]
    return Response(routes)


@api_view(['GET'])
def get_data(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_data(request):
    serializer = CustomUserSerializer(data=request.data)
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']
    username = request.data['username']
    phone_number = request.data['phone_number']
    password = request.data['password']
    if serializer.is_valid():
        CustomUser.objects.create_user(first_name=first_name,username=username,email=email, last_name=last_name, phone_number=phone_number,password=password)
    else:
        serializer.errors
    return Response(serializer.data)

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class=CustomUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class=CustomUserSerializer