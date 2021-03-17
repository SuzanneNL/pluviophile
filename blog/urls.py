from django.contrib import admin
from django.urls import path
from .views import BlogPostsList


urlpatterns = [
    path('', BlogPostsList.as_view(), name="blog_posts")
]
