from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect
from .models import FuelStation, FuelRequest, Delivery
from .forms import FuelRequestForm, DeliveryForm

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')

def login2(request):
    return render(request, 'login2.html')
def login3(request):
    return render(request, 'login3.html')

def fuel_request(request):
    if request.method == 'POST':
        form = FuelRequestForm(request.POST)
        if form.is_valid():
            fuel_request = form.save()
            return render(request, 'fuel_request.html', {'fuel_request': fuel_request})
    else:
        form = FuelRequestForm()
    return render(request, 'fuel_request.html', {'form': form, 'fuel_stations': FuelStation.objects.all()})

def fuel_station(request):
    fuel_requests = FuelRequest.objects.filter(delivery_status='Pending')
    return render(request, 'fuel_station.html', {'fuel_requests': fuel_requests})

def accept_fuel_request(request, fuel_request_id):
    fuel_request = FuelRequest.objects.get(pk=fuel_request_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.fuel_request = fuel_request
            delivery.save()
            fuel_request.delivery_status = 'Accepted'
            fuel_request.save()

            return render(request, 'fuel_request.html',{'fuel_request': fuel_request})
    else:
        form = DeliveryForm()
    return render(request, 'accept_fuel_request.html', {'form': form, 'fuel_request': fuel_request})

def delivery(request):
    fuel_requests = FuelRequest.objects.filter(delivery_status='Accepted')
    return render(request, 'delivery.html', {'fuel_requests': fuel_requests})

def mark_delivery(request, fuel_request_id):
    fuel_request = FuelRequest.objects.get(pk=fuel_request_id)
    fuel_request.delivery_status = 'Delivered'

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.fuel_request = fuel_request
            delivery.save()

    return render(request, 'fuel_request.html', {'fuel_request': fuel_request})
