
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.donate, name='donate'),
    path('charge/', views.charge, name='charge'),
    path('donation_success/', views.donation_success, name='donation_success'),
]