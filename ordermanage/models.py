from django.db import models
from Inventory.models import *

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

class order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(customer, on_delete=models.CASCADE) #relation with customer table,if you delete customer, orders will be deleted
    product_reference = models.ForeignKey(product, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, null=True)
    order_date = models.DateField(null=True)
    quantity= models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

    def __str__(self):
        return self.order_number