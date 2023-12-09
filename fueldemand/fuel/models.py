from django.db import models

# Create your models here.
# models.py

from django.db import models

class FuelStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

class FuelRequest(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    liters = models.FloatField()
    fuel_type = models.CharField(max_length=10, choices=[('petrol', 'Petrol'), ('diesel', 'Diesel')])
    fuel_station = models.CharField(max_length=10, choices=[('hp', 'indian'), ('indian', 'hp')])
    delivery_status = models.CharField(max_length=20, default='Pending')

class Delivery(models.Model):
    fuel_request = models.OneToOneField(FuelRequest, on_delete=models.CASCADE)
    delivery_boy_name = models.CharField(max_length=100)
    delivery_boy_mobile = models.CharField(max_length=15)
