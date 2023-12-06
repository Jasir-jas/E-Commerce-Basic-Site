from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping =True  
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.get_total for item in orderitems ])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.quantity for item in orderitems ])
        return total
    
        
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order,max_length=200,default=0,on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product
    
    
    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total
    
class Shippingaddress(models.Model):
    customer = models.ForeignKey(Customer,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order,max_length=200,on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    
    

    
    