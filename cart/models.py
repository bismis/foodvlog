from django.db import models
from shop.models import *

# Create your models here.
class cartmodel(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.cart_id

class items(models.Model):
    item=models.ForeignKey(products, on_delete=models.CASCADE)
    cart=models.ForeignKey(cartmodel, on_delete=models.CASCADE)
    qnt=models.IntegerField()
    # active=models.BooleanField(default=True)

    def __str__(self):
        return self.item