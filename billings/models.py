from email.policy import default
from statistics import quantiles
from unicodedata import category
from django.db import models

#import settings 
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100,  unique=True)
    imgUrl = models.TextField(default='')

    def __str__(self):
        return self.name
        
class Product(models.Model):
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, null=True, blank=True)
    imgUrl = models.TextField(default='')
    selling_price = models.FloatField(null=True, blank=True)
    actual_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)

    def __str__(self):
        return self.name

    def get_profit(self):
        return self.selling_price - self.actual_price

class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, related_name='stores')
    name = models.CharField(max_length=100)
    imgUrl = models.TextField(null=True, blank=True)
    selling_price = models.FloatField(null=True, blank=True)
    actual_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
     
    def __str__(self):
        return self.name

    def get_profit(self):
        return self.selling_price - self.actual_price
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, related_name='carts')
    get_profit = models.IntegerField(default=1)
    name = models.CharField(max_length=100, default='name')
    imgUrl=models.TextField(default="")
    selling_price= models.FloatField(default=1)
    actual_price= models.FloatField(default=1)
    quantity= models.IntegerField(default=1)
    date= models.CharField(max_length=100, default="")
     
    def __str__(self):
        return self.name







  
