from django.shortcuts import render
from flask import redirect

# Create your views here.

def customerList(request):
    return render(request, 'customer_list.html')

def orderList(request):
    return render(request, 'orders.html')   

def update_order(request, id):
    return render(request, 'update_order.html')

def delete_order(request, id):  
    return render(request, 'delete_order.html')

def ordersAdd(request):

    context={
        "order_form": order_Form()
    }


    if request.method == "POST":
        selected_product = product.objects.get(id =request.POST['product_reference'])

        amount = selected_product.price * float(request.POST['quantity'])

        gst = (amount * selected_product.gst_percentage) / 100

        bill_amount = amount + gst

        new_order = order(customer_reference_id = request.POST['customer'],
                          product_reference_id = request.POST['product_reference'],
                          order_number = request.POST['order_number'],
                          order_date = request.POST['order_date'],
                          quantity = request.POST['quantity'],
                          amount = amount,
                          gst = gst,
                          bill_amount = bill_amount
                          )
        new_order.save()

    return render(request, 'add_orders.html')

def order_list(request):
    context = {
        "orders": orders.objects.all()
    }

    return render(request, 'orders.html', context)    

def orderdelete(request, id):
    order = orders.objects.get(id=id)
    order.delete()
    return redirect('/orders/orders/')

    context = {
        "orders": orders.objects.all()
    }

    return render(request, 'orders.html', context)