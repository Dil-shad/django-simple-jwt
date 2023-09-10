from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
#from .utils import create_jwt_pair_for_user
from rest_framework import status
from django.contrib.auth.models import User,auth
from .models import User

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        #print(email, password)

        response_data = {'email': email, 'password': password}

        user=User.objects.get(email=email,password=password)
        print(user.name)
       # user = authenticate(user)
        

        if user is not None:
            response_data["message"] = "Login Successful"
            response_data["user"] = user.name
            return Response(data=response_data, status=status.HTTP_200_OK)
           
        else:
            response_data["message"] = "Invalid email or password"
            return Response(data=response_data, status=status.HTTP_401_UNAUTHORIZED)







