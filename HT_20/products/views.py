from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Product, ProductCategory


def homepage(request, slug=None):
    data = Product.objects.filter(status=True)

    if slug:
        category = get_object_or_404(ProductCategory, slug=slug)
        data = data.filter(product_category=category)
    context = {
        'data': data,
    }
    return render(request, 'products/homepage.html', context)


def product_details(request, slug):
    data = Product.objects.get(slug=slug)
    context = {
        'data': data,
    }
    return render(request, 'products/product_details.html', context)


@login_required
def add_to_cart(request, slug):
    messages.success(request, 'Product was added!')
    return redirect('/')
