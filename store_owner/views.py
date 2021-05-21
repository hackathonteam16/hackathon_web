from django.shortcuts import render ,redirect
from django.http  import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .filters import ProductFilter

# Create your views here.
from .models import *
from .forms import *
#from .filters import OrderFilter.

def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}

def dashboard(request):
    return  render(request, 'store_owner/dashboard.html')

def new_product(request):
    products = Product.objects.all()
    return  render(request, 'store_owner/new_product.html',{'products' : products})

def update_product(request):
    products = Product.objects.all()
    return  render(request, 'store_owner/update_product.html',{'products' : products})

def my_products(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'store_owner/my_products.html', context)

def shop_owner(request):
    return  render(request, 'store_owner/shop_owner.html')

def status(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='הגיע אל הלקוח').count()
    pending = orders.filter(status='בטיפול').count()
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return  render(request, 'store_owner/status.html', context)



def new_shop(request):
    shop = Product.objects.all()
    return  render(request, 'store_owner/new_shop.html',{'shop' : shop})

def customers(request):
    customer = Customer.objects.get()
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request, 'store_owner/customers.html',context)

def createShop(request):
    form = ShopForm()
    if request.method == 'POST' :
        form = ShopForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'store_owner/product_form.html', context)

def createProduct(request):
    form = OrderForm()
    if request.method == 'POST' :
        form = OrderForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('/dashboard')
    context = {'form':form}
    return render(request, 'store_owner/product_form.html', context)

def updateProduct(request,pk):
    product = Product.objects.get(id = pk)
    form = OrderForm(instance=product)
    if request.method == 'POST' :
         form = OrderForm(request.POST, instance= product)
         if form.is_valid():
             form.save()
             return redirect('/my_products')
    context = {'form': form}
    return render(request, 'store_owner/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/my_products')
    context = {'item':product}
    return render(request, 'store_owner/delete.html', context)
