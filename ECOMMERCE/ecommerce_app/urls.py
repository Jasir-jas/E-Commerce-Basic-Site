from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart,name="cart"),
    path("checkout/", views.checkout,name="checkout"),
    path("update_items/", views.updateItems,name="update_items"),
    # path("products/<int:pk>/", views.product, name="products"),
    
]