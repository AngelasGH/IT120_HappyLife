from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import json


# user_view
def user_home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'user/home.html', context)


def user_products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    user_product = Product.objects.all()
    context = {'product': user_product, 'cartItems': cartItems}
    return render(request, 'user/products.html', context)


def user_view_products(request):
    context = {}
    return render(request, 'user/green_tea.html', context)


def user_view_products_details(request):
    context = {}
    return render(request, 'user/green_tea_details.html', context)


def user_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'user/cart.html', context)


def user_checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'user/checkout.html', context)


def user_faqs(request):
    context = {}
    return render(request, 'user/faqs.html', context)


def user_about_us(request):
    context = {}
    return render(request, 'user/about_us.html', context)


def user_contact_us(request):
    context = {}
    return render(request, 'user/contact_us.html', context)


def user_register(request):
    context = {}
    return render(request, 'Register_login/register.html', context)


def user_login(request):
    context = {}
    return render(request, 'Register_login/login.html', context)


def user_reset(request):
    context = {}
    return render(request, 'Register_login/reset.html', context)


def user_verification(request):
    context = {}
    return render(request, 'Register_login/verification.html', context)


def user_reset_password(request):
    context = {}
    return render(request, 'Register_login/reset_password.html', context)


def user_successfully_reset(request):
    context = {}
    return render(request, 'Register_login/successfully_reset.html', context)


def user_reviews(request):
    context = {}
    return render(request, 'user/reviews.html', context)


def user_butterfly(request):
    user_product = Product.objects.all()
    context = {'product': user_product}
    return render(request, 'user_view_products/butterfly.html', context)


def user_butterfly_details(request):
    context = {}
    return render(request, 'user_view_products/butterfly_details.html', context)


def user_chamomile(request):
    context = {}
    return render(request, 'user_view_products/chamomile.html', context)


def user_chamomile_details(request):
    context = {}
    return render(request, 'user_view_products/chamomile_details.html', context)


def user_green_tea(request):
    context = {}
    return render(request, 'user_view_products/green_tea.html', context)


def user_green_tea_details(request):
    context = {}
    return render(request, 'user_view_products/green_tea_details.html', context)


def user_lapsang(request):
    context = {}
    return render(request, 'user_view_products/lapsang.html', context)


def user_lapsang_details(request):
    context = {}
    return render(request, 'user_view_products/lapsang_details.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    if action == 'delete':
        orderItem.delete()

    return JsonResponse('item was added', safe=False)

