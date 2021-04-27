from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.donate, name='donate'),
    path('charge/', views.charge, name='charge'),
    path('donation_success/<donation_number>', views.donation_success,
         name='donation_success'),
    path('wh/', webhook, name='webhook'),
    path('error', views.error, name='error'),
]
