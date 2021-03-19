from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


class BlogPostsListView(ListView):
    model = BlogPost
    template_name = "blog/blog_posts_list.html"


class BlogPostView(DetailView):
    model = BlogPost
    template_name = "blog/blog_post.html"
