from django.shortcuts import render
from .models import * 

# Create your views here.
def store(request):
    products = Product.objects.all()
    
    context = {'products':products}
    return render(request,"ecommerce_app/store.html",context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}
    context = {'items':items,'order':order}
    return render(request,"ecommerce_app/cart.html",context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}
    context = {'items':items,'order':order}
    return render(request,"ecommerce_app/checkout.html",context)
