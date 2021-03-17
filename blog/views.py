from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost


class BlogPostsList(ListView):
    model = BlogPost
    template_name = "blog/blog_posts_list.html"
