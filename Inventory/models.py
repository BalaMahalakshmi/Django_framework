from django.db import models

class product(models.Model):

    pro_name = models.CharField(max_length=100, null=True)
    pro_code = models.CharField(max_length=50, null=True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    stock = models.BooleanField(default=False)

    def __str__(self):
        return self.pro_name + " - " + self.pro_code