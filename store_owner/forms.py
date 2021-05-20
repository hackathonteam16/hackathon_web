from django.forms import ModelForm
from .models import Product
class OrderForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','category','description','size']
