from django.forms import ModelForm
from .models import *

class productForm(ModelForm):
    class Meta:
        model = product
        fields = '__all__'   #specific fields using like this = ['name', 'price']