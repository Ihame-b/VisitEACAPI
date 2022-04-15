from django.db import models
from sys import maxsize
from tracemalloc import start
from unicodedata import category
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here. 
User =get_user_model()

class Product(models.Model):

    country=(
        ('RWANDA','rwanda'),
        ('Uganda','uganda'),
        ('BURUNDI','burundi'),
        ('CONGO','congo'),
     )

    category=(
        ('VORCANOES','vorcanoes'),
        ('HOTEL','hotel'),
        ('HILLS','hills')
    )

    status=(
        ('FREE','free'),
        ('NOT FREE','not free')
    )

    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    productname = models.CharField(max_length=200, null=False, blank=False)
    campanyemail = models.EmailField(max_length=100, null=False, blank=False)
    phone = PhoneNumberField (max_length=20, null=False, blank=False)
    country = models.CharField(max_length=25,choices=country,default=country[0][0])
    category = models.CharField(max_length=25,choices=category,default=category[0][0])
    image =models.ImageField(upload_to='product_image', null=True, blank= True)
    payment =models.CharField(max_length=25,choices=status,default=status[0][0])
    description = models.CharField(max_length=10000)
    placed_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Product {self.productname} by {self.customer.id}"
