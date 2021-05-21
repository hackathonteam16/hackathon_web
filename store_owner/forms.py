from django.forms import ModelForm
from .models import *
from django import forms

class OrderForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['name','price','category','description','size','picture']


class ShopForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #category = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Shop
        fields = ['name','category']

