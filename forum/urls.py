from django.contrib import admin
from django.urls import path
from .views import Forum


urlpatterns = [
    # path('', views.forum, name="forum")
    path('', Forum.as_view(), name="forum"),
]
