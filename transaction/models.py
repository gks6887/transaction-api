from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Transaction(models.Model):

    class Payment(models.IntegerChoices):
        DEBIT = 0
        CREDIT = 1
        CASH = 2

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    tx_at = models.DateTimeField(auto_now_add=True) # read only
    payment_method = models.IntegerField(choices=Payment)

    def __str__(self):
        return "Transaction(ID: %s) - %s" %(self.id, self.tx_at)
