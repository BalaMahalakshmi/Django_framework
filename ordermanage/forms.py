from django.forms import ModelForm
from .models import *

class customer_Form(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'   #specific fields using like this = ['name', 'email', 'phone']


class order_Form(ModelForm):
    class Meta:
        model = order
        fields = ['customer', 'product_reference', 'order_number', 'order_date', 'quantity']   #specific fields using like this = ['customer', 'product_reference', 'order_number', 'order_date', 'quantity', 'amount', 'gst', 'bill_amount']