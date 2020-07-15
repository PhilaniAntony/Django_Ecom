from django.shortcuts import render
from .models import *

def store_view(request):
    products = Product.objects.all()
    context = {'products': products,}
    return render(request, 'store/store.html', context)


def cart_view(request):
    if request.user.is_authenticated :
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items' : items,
        'order' : order ,
    }
    return render(request, 'store/cart.html', context)



def checkout_view(request):
    if request.user.is_authenticated :
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items' : items,
        'order' : order ,
    }
    return render(request, 'store/checkout.html', context)
