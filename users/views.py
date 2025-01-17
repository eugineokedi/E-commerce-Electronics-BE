from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user

# Create your views here.

class UserViewList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class UserViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
    
class UserLoginView(APIView):
    # Implement login functionality here
    def post(self, request: Request, *args, **kwargs):
        # Extract data from incoming request
        data = request.data
        email = data.get('email')
        password = data.get('password')
        
        # Authenticate user
        user = authenticate(email=email, password=password)
        
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login successful",
                "token": tokens
            } 
            return Response(data=response, status=status.HTTP_200_OK)  
        
        else:
            response = {
                "message": "Invalid email or password",
                "data": {}
            }
            return Response(data=response, status=status.HTTP_401_UNAUTHORIZED) 
        
    
    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data = content, status=status.HTTP_200_OK)       
