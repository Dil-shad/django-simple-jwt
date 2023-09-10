from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import SignUpSerializer, BookSerializer
from .tokens import create_jwt_pair_for_user
from .models import Books
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            return Response(
                {"message": "Login Successful", "tokens": tokens},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Invalid email and password"},
                status=status.HTTP_401_UNAUTHORIZED
            )


class BooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Books.objects.all()
        serialized = BookSerializer(books, many=True)
        return Response(serialized.data)
    
    
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def books_view(request):
#     books = Books.objects.all()
#     serialized = BookSerializer(books, many=True)
#     return Response(serialized.data)