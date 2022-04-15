from email import message
from itertools import product
from xmlrpc.client import ResponseError
from django.shortcuts import render,get_object_or_404
from requests import delete
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Product, User
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

from TouristProduct import serializers

# Create your views here.

class helloProductView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Hello Tourist")
    def get(self, request):
        return Response(data= {"message":"hello product"}, status=status.HTTP_200_OK)


class ProductCreationListView(generics.GenericAPIView):
    serializer_class=serializers.ProductCreationSerializer
    queryset=Product .objects.all()
    # permission_class=[IsAuthenticated]
    #permission_class=[IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(operation_summary="List all Tourist areas")
    def get(self, request):
        product=Product.objects.all()
        serializer=self.serializer_class(instance=product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Create new Tourist site")    
    def post(self, request):
        data=request.data
        serializer=self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProductDetailsView(generics.GenericAPIView):
    serializer_class=serializers.ProductCreationSerializer
    permission_class=[IsAdminUser]

    @swagger_auto_schema(operation_summary="Retreave Tourist site by id")
    def get(self, request, Product_id):
        product = get_object_or_404(Product, pk=Product_id)
        serializer=self.serializer_class(instance=product)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Updating Tourist site by id")
    def put(self, request, Product_id):
        data =request.data
        product=get_object_or_404(Product, pk=Product_id)
        serializer=self.serializer_class(data=data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

        # user = request.user
        # serializer=self.serializer_class(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(data=serializer.data, status=status.HTTP_200_OK)

        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    @swagger_auto_schema(operation_summary="Delete Tourist site by id")
    def delete(self, request, Product_id):
        product=get_object_or_404(Product, pk=Product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateProductCategory(generics.GenericAPIView):
    serializer_class =serializers.ProductCategoryUpdateSerializer
    Permission_classes=[IsAdminUser]
    
    @swagger_auto_schema(operation_summary="Update Tourist category by id")
    def put(self, request, Product_id):
        product=get_object_or_404(Product, pk=Product_id)
        data=request.data
        serializer=self.serializer_class(data=data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class UserProductView(generics.GenericAPIView):
    serializer_class=serializers.ProductDetailsSerializer

    @swagger_auto_schema(operation_summary="Get all Tourist site of given user ")
    def get(self,request, user_id):
        user=User.objects.get(pk=user_id)

        product=Product.objects.all().filter(customer=user)
        serializer=self.serializer_class(instance=product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserProductDetails(generics.GenericAPIView):
    serializer_class=serializers.ProductDetailsSerializer

    @swagger_auto_schema(operation_summary="Get a Tourist site to a specific user")
    def get(self, request, user_id, product_id):
         user=User.objects.get(pk=user_id)
        # product=Product.objects.all().filter(customer=user).filter(pk=product_id)
         product =Product.objects.all().filter(customer=user).get(pk=product_id)
         serializer=self.serializer_class(instance=product)
         return Response(data=serializer.data, status=status.HTTP_200_OK)