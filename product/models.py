from django.db import models
from django.utils import timezone
from uuid import uuid4

def generate_uid():
    date=timezone.now().strftime("%Y%m%d")
    uid="PROD-%s-%s" %(date, uuid4())
    return uid

class Product(models.Model):
    uid = models.CharField(
        editable=False, 
        unique=True, 
        default=generate_uid, 
        max_length=255
    )   # Need to prevent being editied via code by other developers.
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "Product: %s - $%s" %(self.name, self.price)


# class ProductState(models.Model):
#     product = models.ForeignKey()
#     stock = models.IntegerField()
#     is_on_sale = models.BooleanField()
#     is_sold_out = models.BooleanField()