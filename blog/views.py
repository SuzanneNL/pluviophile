from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostsListView(ListView):
    model = BlogPost
    template_name = "blog/blog_posts_list.html"
    paginate_by = 4


class BlogPostView(DetailView):
    model = BlogPost
    template_name = "blog/blog_post.html"


class AdminRequiredMixin (LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('error')


class AddBlogPostView(AdminRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/add_blog_post.html"

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class EditBlogPostView(AdminRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/edit_blog_post.html"


class DeleteBlogPostView(AdminRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "blog/delete_blog_post.html"
    success_url = reverse_lazy('blog')


def LikeView(request, pk):
    blogpost = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    liked = False
    if blogpost.likes.filter(id=request.user.id).exists():
        blogpost.likes.remove(request.user)
        liked = False
    else:
        blogpost.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog_post', args=[str(pk)]))


def error(request):
    return render(request, 'blog/error.html')
