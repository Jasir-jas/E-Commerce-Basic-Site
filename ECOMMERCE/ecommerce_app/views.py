from django.shortcuts import render
from .models import * 

# Create your views here.
def store(request):
    products = Product.objects.all()
    
    context = {'products':products}
    return render(request,"ecommerce_app/store.html",context)

def cart(request):
    context = {}
    return render(request,"ecommerce_app/cart.html",context)

def checkout(request):
    context = {}
    return render(request,"ecommerce_app/checkout.html",context)
