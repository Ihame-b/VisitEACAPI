from email import message
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import User
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class helloAuthView(generics.GenericAPIView):
    
    @swagger_auto_schema(operation_summary="Hello Auth")
    def get(self, request):
        return Response(data= {"message":"hello auther"}, status=status.HTTP_200_OK)

class UserCreationView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    
    @swagger_auto_schema(operation_summary="create user account")
    def post(self, request):
        data=request.data

        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    