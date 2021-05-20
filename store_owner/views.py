from django.shortcuts import render
from django.http  import HttpResponse
#from django.forms import inlinefomset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
#from .forms import OrderForm
#from .filters import OrderFilter

def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}

def home(request):
    return  render(request, 'store_owner/dashboard.html')

def new_product(request):
    products = Product.objects.all()
    return  render(request, 'store_owner/new_product.html',{'products' : products})

def update_product(request):
    products = Product.objects.all()
    return  render(request, 'store_owner/update_product.html',{'products' : products})

def my_products(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    products = Product.objects.all()
    return render(request, 'store_owner/my_products.html', context)



def status(request):
    return  render(request, 'store_owner/status.html')

def new_shop(request):
    return  render(request, 'store_owner/new_shop.html')
