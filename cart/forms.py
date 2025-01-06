# forms.py
from django import forms
from .models import PlaceOrder  

class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = PlaceOrder
        fields = ['name', 'address', 'district', 'pincode', 'country', 'contact', 'total_price'  ]


