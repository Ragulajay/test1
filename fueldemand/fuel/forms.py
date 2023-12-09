# forms.py

from django import forms
from .models import FuelRequest, Delivery

class FuelRequestForm(forms.ModelForm):
    class Meta:
        model = FuelRequest
        fields = ['name', 'mobile_no', 'location', 'liters', 'fuel_type', 'fuel_station']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['delivery_boy_name', 'delivery_boy_mobile']
