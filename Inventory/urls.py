from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
    path('home/', inventory_home),
    path('about/', inventory_about),
    path('services/', inventory_services),  
    path('contact/', inventory_contact),
]