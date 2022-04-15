from dataclasses import fields
from email.policy import default
from xml.parsers.expat import model
from .models import Product
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class ProductCreationSerializer(serializers.ModelSerializer):

    productname = serializers.CharField(max_length=200)
    campanyemail = serializers.EmailField(max_length=100)
    phone = PhoneNumberField (max_length=20)
    country = serializers.CharField(max_length=25,default='eac')
    category = serializers.CharField(max_length=25,default='better')
    image =serializers.ImageField()
    payment =serializers.CharField(max_length=25,default='free')
    description = serializers.CharField(max_length=10000)
    class Meta:
        model=Product
        fields='__all__'
        #field=['productname','campanyemail','phone','country','category','image','payment','description']

class ProductDetailsSerializer(serializers.ModelSerializer):

    productname = serializers.CharField(max_length=200)
    campanyemail = serializers.EmailField(max_length=100)
    phone = PhoneNumberField (max_length=20)
    country = serializers.CharField(max_length=25,default='eac')
    category = serializers.CharField(max_length=25)
    image =serializers.ImageField()
    payment =serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=10000)
    placed_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    class Meta:
        model=Product
        fields=['id','productname','campanyemail','phone','country','category','image','payment','description','placed_at','updated_at']



class ProductCategoryUpdateSerializer(serializers.ModelSerializer):
    product_category=serializers.CharField()
    class Meta:
        model=Product
        fields=['product_category']