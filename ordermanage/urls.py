from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path('customers/', customerList),
    path('orders/', orderList),
    path('Update-order/<str:id>/', update_order, name="update_order"),
    path('Delete-order/<str:id>/', delete_order, name="delete_order"),
    path('add/orders/',ordersAdd),
    path('delete/orders/<str:id>/',delete_order),
]