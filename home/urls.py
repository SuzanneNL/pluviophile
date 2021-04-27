from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('rain', views.rain, name='rain'),
]
