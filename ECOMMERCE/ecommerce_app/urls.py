from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart,name="cart"),
    path("checkout/", views.checkout,name="checkout"),
    path("update_items/", views.updateItems,name="update_items"),
    path("process_order/", views.processOrder,name="process_order"),
    # path("payment_success/", views.payment_success,name="payment_success"),
    
    
]