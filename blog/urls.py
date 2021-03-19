from django.contrib import admin
from django.urls import path
from .views import BlogPostsListView, BlogPostView, AddBlogPostView


urlpatterns = [
    path('', BlogPostsListView.as_view(), name="blog_posts"),
    path('blogpost/<int:pk>', BlogPostView.as_view(), name="blog_post"),
    path('add_blogpost/', AddBlogPostView.as_view(), name="add_blog_post"),
]
