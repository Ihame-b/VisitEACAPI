from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloAuthView.as_view(),name='hello_auth'),
    path('signup/', views.UserCreationView.as_view(),name='signup'),
]
