from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['productname', 'category', 'image', 'placed_at']
    list_filter =['campanyemail', 'placed_at', 'updated_at', 'country']