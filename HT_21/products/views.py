from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, ProductCategory, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.all()


def homepage(request, slug=None):
    data = Product.objects.filter(status=True)

    if slug:
        category = get_object_or_404(ProductCategory, slug=slug)
        data = data.filter(product_category=category)
    context = {
        'data': data,
    }
    return render(request, 'products/homepage.html', context)


def product_details(request, pk):
    data = Product.objects.get(pk=pk)
    context = {
        'data': data,
    }
    return render(request, 'products/product_details.html', context)


@login_required
def add_to_cart(request, pk):
    context = {}
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.setdefault('cart', {})
    products = cart.setdefault('products', [])
    products.append(pk)
    cart_total = cart.get('total') or 0
    product.save()
    cart['total'] = cart_total + round(float(product.product_price), 2)
    request.session.modified = True
    context['data'] = products
    return JsonResponse(context)


@login_required
def cart(request):
    if not request.session.get('cart'):
        context = {}
        return render(request, 'products/cart.html', context)
    cart = request.session.get('cart')
    data = [Product.objects.get(pk=pk) for pk in cart['products']]
    context = {
        'data': data,
        'total': cart['total'],
    }
    return render(request, 'products/cart.html', context)

@login_required()
def commit_order(request):
    cart = request.session.get('cart')
    if not cart['products']:
        messages.error(request, 'Order failed!')
        return redirect('products:cart')
    new_order = Order()
    new_order.user_id = request.user
    new_order.order_items_ids = cart['products']
    new_order.total_cost = cart['total']
    new_order.save()
    del request.session['cart']
    messages.success(request, 'Order completed!')
    return redirect('products:cart')


@login_required()
def clear_cart(request):
    if request.session.get('cart'):
        del request.session['cart']
    return redirect('products:cart')
