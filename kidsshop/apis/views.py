from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from product.models import Product

# Create your views here.

def get_information(request):
    data = { 
        'products': 'this url gives you all the products\' information'
    }

    return JsonResponse(data)

@api_view(['Get'])
def products(request):
    products = Products.objects.all()