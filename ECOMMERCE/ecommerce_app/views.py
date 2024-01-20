from django.shortcuts import render,redirect
from .models import * 
from django.http import JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from json.decoder import JSONDecodeError
from . utils import cookieCart,cartData,guestOrder
from django.conf import settings
import razorpay

# Create your views here.
@csrf_exempt
def store(request):
    # data = cartData(request)
    # print(data)
    # cartItems = data['cartItems']
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,"ecommerce_app/store.html",context)

@csrf_exempt
def cart(request):
    # data = cartData(request)
    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
                 
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,"ecommerce_app/cart.html",context)

@csrf_exempt
def checkout(request):
    # data = cartData(request)
    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        print(cartItems)
        order = cookieData['order']
        print(order)
        items = cookieData['items']
        print(items)
    
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,"ecommerce_app/checkout.html",context)



@csrf_exempt
def updateItems(request):
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    print('productId:',productId)
    action = data['action']
    print('action:',action)
    
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer = customer, completed=False)
    orderItem,created= OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.quantity= (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity= (orderItem.quantity - 1)
    orderItem.save()
        
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was added',safe=False)

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    print(data)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, completed=False)
        

            
        # this is for guest users
    else:
        customer, order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    
    if total == order.get_cart_total:
         order.completed=True
    order.save()
    
    if order.shipping == True:
        Shippingaddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
            )
    
         
    return JsonResponse('payment submitted',safe=False)
