from django.forms import ModelForm
from .models import Product
from django import forms

class OrderForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['name','price','category','description','size']
