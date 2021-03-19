from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostsListView(ListView):
    model = BlogPost
    template_name = "blog/blog_posts_list.html"


class BlogPostView(DetailView):
    model = BlogPost
    template_name = "blog/blog_post.html"


class AddBlogPostView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/add_blog_post.html"

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
