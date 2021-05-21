from django.shortcuts import render
from store_owner.models import *
from store_owner.filters import ProductFilter

# Create your views here.
def home(request):
    return  render(request, 'mall/home_page.html')

def shops(request):
    shop = Shop.objects.all()
    context = {'shop' : shop}
    return render(request, 'mall/stores.html', context)

def store_products(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {'products': products, 'myFilter':myFilter}
    return render(request, 'mall/stores_products.html', context)