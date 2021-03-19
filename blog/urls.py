from django.contrib import admin
from django.urls import path
from .views import BlogPostsListView, BlogPostView


urlpatterns = [
    path('', BlogPostsListView.as_view(), name="blog_posts"),
    path('blogpost/<int:pk>', BlogPostView.as_view(), name="blog_post"),
]
