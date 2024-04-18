from django.shortcuts import render, redirect, get_object_or_404
from flipkartapp.models import product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart



def add_cart(request,product_id):
    products=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=cart_id(request)

        )
        cart.save(),
    try:
        cart_item=CartItem.objects.get(product=products,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=products,
            quantity=1,
            cart=cart

        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter +=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(product=products,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return  redirect('cart:cart_detail')


def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    products = get_object_or_404(product, id=product_id)
    cart_item = CartItem.objects.get(product=products, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')



# from django.shortcuts import render, redirect, get_object_or_404
# from flipkartapp.models import Product
# from .models import Cart, CartItem
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.sessions.models import Session
#
#
# def get_or_create_cart_id(request):
#     cart_id = request.session.session_key
#     if not cart_id:
#         request.session.create()
#         cart_id = request.session.session_key
#     return cart_id
#
#
# def add_to_cart(request, product_id):
#     products = get_object_or_404(Product, id=product_id)
#     cart_id = get_or_create_cart_id(request)
#     cart, created = Cart.objects.get_or_create(cart_id=cart_id)
#
#     try:
#         cart_item = CartItem.objects.get(product=products, cart=cart)
#         if cart_item.quantity < products.stock:
#             cart_item.quantity += 1
#             cart_item.save()
#     except CartItem.DoesNotExist:
#         CartItem.objects.create(product=products, quantity=1, cart=cart)
#
#     return redirect('cart:cart_detail')
#
#
# def cart_detail(request):
#     total = 0
#     counter = 0
#     cart_items = []
#
#     cart_id = get_or_create_cart_id(request)
#     try:
#         cart = Cart.objects.get(cart_id=cart_id)
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#         for cart_item in cart_items:
#             total += cart_item.product.price * cart_item.quantity
#             counter += cart_item.quantity
#     except ObjectDoesNotExist:
#         pass
#
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total': total, 'counter': counter})
#
#
# def remove_from_cart(request, product_id):
#     cart_id = get_or_create_cart_id(request)
#     cart = get_object_or_404(Cart, cart_id=cart_id)
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         cart_item = CartItem.objects.get(product=product, cart=cart)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#     except CartItem.DoesNotExist:
#         pass
#
#     return redirect('cart:cart_detail')
#
#
# def remove_all_from_cart(request, product_id):
#     cart_id = get_or_create_cart_id(request)
#     cart = get_object_or_404(Cart, cart_id=cart_id)
#     products = get_object_or_404(Product, id=product_id)
#     try:
#         cart_item = CartItem.objects.get(product=products, cart=cart)
#         cart_item.delete()
#     except CartItem.DoesNotExist:
#         pass
#
#     return redirect('cart:cart_detail')
