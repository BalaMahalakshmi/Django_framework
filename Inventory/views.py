from django.shortcuts import render, redirect
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

def all_products(request):

    context = {
        "all_pro": product.objects.all()
    }   

    return render(request, 'allprod.html', context)

def delete_product(request, id):
    selected_pro = product.objects.get(id = id)
    selected_pro.delete()
    return redirect('/home/all-products/')

def update_product(request, id):
    selected_pro = product.objects.get(id = id)

    context = {
        "pro_form": productForm(instance=selected_pro)
    }

    if request.method == "POST":
        pro_form = productForm(request.POST, instance=selected_pro)
        if pro_form.is_valid():
            pro_form.save()
            return redirect('/home/products/')
        
    return render(request, 'products.html', context)