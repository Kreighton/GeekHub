from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

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
