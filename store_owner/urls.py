from django.urls import path
from . import views
from mall import views as mall_views

urlpatterns = [
    path('', mall_views.home),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('new_product/', views.createProduct, name = 'new_product'),
    path('update_product/', views.updateProduct, name = 'update_product'),
    path('my_products/', views.my_products, name = 'my_product'),
    path('status/', views.status, name = 'status'),
    path('new_shop/', views.new_shop, name = 'new_shop'),
    path('customers/', views.customers, name = 'customers'),
    path('delete_order/<str:pk>', views.deleteProduct, name='delete_product'),
    #path('create_product/', views.createProduct, name = 'create_product'),

]
