from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self):
        return self.user
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    #image
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
class Shippingaddress(models.Model):
    customer = models.ForeignKey(Customer,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    
    

    
    