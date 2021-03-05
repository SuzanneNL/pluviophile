from django.contrib import admin
from django.urls import path
from .views import (
    ForumView,
    ThreadView,
    StartThreadView,
    EditThreadView,
    DeleteThreadView,
)

urlpatterns = [
    path('', ForumView.as_view(), name="forum"),
    path('thread/<int:pk>', ThreadView.as_view(), name="thread"),
    path('start_thread/', StartThreadView.as_view(), name="start_thread"),
    path('thread/edit/<int:pk>', EditThreadView.as_view(), name="edit_thread"),
    path('thread/delete/<int:pk>', DeleteThreadView.as_view(), name="delete_thread"),
]
