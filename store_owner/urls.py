from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('new_product/', views.new_product),
    path('update_product/', views.update_product),
    path('my_products/', views.my_products),
    path('status/', views.status),
    path('new_shop/', views.new_shop),
]
