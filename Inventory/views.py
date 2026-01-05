from django.shortcuts import render
from .models import *
from .forms import *

def inventory_home(request):

    context = {
        "name": "Mahabi",
        "role": "employee",
        "numbers": [10, 20, 30, 40, 50],
        "age": 22,
        "city":{"MB":"Theni", "MA":"UDT"},
    }
    return render(request, 'index.html', context)

def inventory_about(request):
    return render(request, 'about.html')

def inventory_services(request):
    return render(request, 'services.html')

def inventory_contact(request):
    return render(request, 'contact.html')

def inventory_products(request):

    context = {
        "products": productForm()
    }   

    if request.method == "POST":
        proForm = productForm(request.POST)
        if proForm.is_valid():
            proForm.save()
       
    return render(request, 'products.html', context)