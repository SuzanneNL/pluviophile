from django.contrib import admin
from django.urls import path
from .views import Forum, Thread


urlpatterns = [
    path('', Forum.as_view(), name="forum"),
    path('thread/<int:pk>', Thread.as_view(), name="thread"),
]
