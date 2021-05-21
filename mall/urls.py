from django.urls import path
from store_owner import views as store_owner_views
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', store_owner_views.dashboard, name = 'dashboard'),
    path('new_product/', store_owner_views.new_product, name='new_product'),
    path('update_product/', store_owner_views.update_product, name='update_product'),
    path('my_products/', store_owner_views.my_products, name='my_product'),
    path('status/', store_owner_views.status, name='status'),
    path('new_shop/', store_owner_views.new_shop, name='new_shop'),
    path('customers/', store_owner_views.customers, name='customers'),
    path('create_product/', store_owner_views.createProduct, name='create_product'),
    path('stores/', views.shops, name = 'stores'),
    path('store_products/', views.store_products, name = 'store_products'),


]