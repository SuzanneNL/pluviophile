from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    ForumView,
    ThreadView,
    StartThreadView,
    EditThreadView,
    DeleteThreadView,
    AddCommentView,
    EditCommentView,
)

urlpatterns = [
    path('', ForumView.as_view(), name="forum"),
    path('thread/<int:pk>', ThreadView.as_view(), name="thread"),
    path('start_thread/', StartThreadView.as_view(), name="start_thread"),
    path('thread/edit/<int:pk>', EditThreadView.as_view(), name="edit_thread"),
    path('thread/delete/<int:pk>', DeleteThreadView.as_view(), name="delete_thread"),
    path('thread/<int:pk>/add_comment/', AddCommentView.as_view(), name="add_comment"),
    path('edit_comment/<int:pk>', EditCommentView.as_view(), name="edit_comment"),
    path('error', views.error, name='error')
]