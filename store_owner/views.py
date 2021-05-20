from django.shortcuts import render
from django.http  import HttpResponse
from django.forms import inlinefomset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
def home(request):
    return  render(request, 'store_owner/dashboard.html')

def new_product(request):
    return  render(request, 'store_owner/new_product.html')

def update_product(request):
    return  render(request, 'store_owner/update_product.html')

def my_products(request):
    return  render(request, 'store_owner/my_products.html')

def status(request):
    return  render(request, 'store_owner/status.html')
