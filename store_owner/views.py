from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return  render(request, 'store_owner/dashboard.html')

def new_product(request):
    return  render(request, 'store_owner/new_product.html')

def update_product(request):
    return  render(request, 'store_owner/update_product.html')

def my_products(request):
    return  render(request, 'store_owner/my_products.html')
