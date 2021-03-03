from django.contrib import admin
from django.urls import path
from .views import ForumView, ThreadView


urlpatterns = [
    path('', ForumView.as_view(), name="forum"),
    path('thread/<int:pk>', ThreadView.as_view(), name="thread"),
]
