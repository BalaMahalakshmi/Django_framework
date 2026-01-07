from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
    path('home/', inventory_home),
    path('about/', inventory_about),
    path('services/', inventory_services),  
    path('contact/', inventory_contact),
    path('products/', inventory_products),
    path('all-products/', all_products),
    path('all-products/delete-product/<int:id>/', delete_product, name='product_delete'),
    path('all-products/update-product/<int:id>/', update_product, name='product_update'),

]