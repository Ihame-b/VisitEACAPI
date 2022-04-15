from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.helloProductView.as_view(),name='hello_auth'),
    path('', views.ProductCreationListView.as_view(),name='product'),
    path('<int:Product_id>/', views.ProductDetailsView.as_view(), name='product_details'),
    path('update-category/<int:Product_id>/', views.UpdateProductCategory.as_view(), name='Update_Product_Category'),
    path('user/<int:user_id>/product/', views.UserProductView.as_view(), name='users_products'),
    path('user/<int:user_id>/product/<int:product_id>', views.UserProductDetails.as_view(), name='users_specific_pdoduct')

]
