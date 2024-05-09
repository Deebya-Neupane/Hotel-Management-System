from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer,GroupSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomModelPermission

# Create your views here.
class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def register(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            hash_password = make_password(password)
            a = serializer.save()
            a.password = hash_password
            a.save()
            return Response('User created successfully!')
        else:
            return Response(serializer.errors)
        
    def login(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email,password=password)
        if user == None:
            return Response('Invalid credentials!')
        else:
            token,_ = Token.objects.get_or_create(user=user)
            return Response(f"Login Successfull, Welcome!! User-{user.id} token : {token.key}")

