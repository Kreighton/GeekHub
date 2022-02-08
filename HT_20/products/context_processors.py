from django.shortcuts import render

from .models import ProductCategory

def categories(request):
    categories = ProductCategory.objects.all()
    return {"categories": categories}