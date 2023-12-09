# urls.py

from django.urls import path
from .views import login,login2,login3, index,home, fuel_request, fuel_station, accept_fuel_request, delivery, mark_delivery

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('fuel_st_login/', login2, name='login2'),
    path('delivery_login/', login3, name='login3'),
    path('fuel_request/', fuel_request, name='fuel_request'),
    path('fuel_station/', fuel_station, name='fuel_station'),
    path('accept_fuel_request/<int:fuel_request_id>/', accept_fuel_request, name='accept_fuel_request'),
    path('delivery/', delivery, name='delivery'),
    path('mark_delivery/<int:fuel_request_id>/', mark_delivery, name='mark_delivery'),
]
