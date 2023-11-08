from django.http import request
from django.shortcuts import render
from products.models import *


def index(request):
    context = {
        'title': 'Home',
        'description': "Description of the home page",
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request , 'products/products.html', context)
