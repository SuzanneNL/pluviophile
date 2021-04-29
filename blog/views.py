# Source: This app was largely influenced by tutorials
# from CoreyMS and John Elder. See README file under 'Sources'.

from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from sortable_listview import SortableListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import BlogPost
from .forms import BlogPostForm


# Source SortableListView: django-sortable-listview documentation
# See README file under 'Sources'
class BlogPostsListView(LoginRequiredMixin, SortableListView):
    """
    This renders a list of all blog posts. Login is required. It is paginated,
    and there are multiple sorting options.
    """
    model = BlogPost
    template_name = "blog/blog_posts_list.html"
    paginate_by = 4
    allowed_sort_fields = {'date_created': {'default_direction': '-',
                                            'verbose_name': 'Date'},
                           'title': {'default_direction': '',
                                     'verbose_name': 'Title'}
                           }
    default_sort_field = 'date_created'


class BlogPostView(LoginRequiredMixin, DetailView):
    """
    This renders a single blog posts. Login is required.
    """
    model = BlogPost
    template_name = "blog/blog_post.html"


# Source for custom Mixin: StackOverFlow. See README file under 'Sources'.
class AdminRequiredMixin (LoginRequiredMixin, UserPassesTestMixin):
    """
    This is a custom mixin, that allows superusers to access pages and peform
    CRUD-actions. Others will be redirected to the error page.
    """
    def test_func(self):
        return self.request.user.is_superuser

    # Source for redirecting: StackOverFlow. See README file under 'Sources'.
    def handle_no_permission(self):
        return redirect('error')


class AddBlogPostView(AdminRequiredMixin, SuccessMessageMixin, CreateView):
    """
    This renders a page with a form for adding a blog post, which can only be
    accessed by superusers. This view inherits from CreateView, which handles
    the creation of the blog post. After creation, a success message appears.
    """
    model = BlogPost
    form_class = BlogPostForm
    success_message = "Blog post '%(title)s' was created successfully"
    template_name = "blog/add_blog_post.html"

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class EditBlogPostView(AdminRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    This renders a page for confirming a blog post, which can only be
    accessed by superusers. This view inherits from UpdateView, which handles
    the updating of the blog post. After the update, a success message appears.
    """
    model = BlogPost
    form_class = BlogPostForm
    success_message = "Blog post '%(title)s' was updated successfully"
    template_name = "blog/edit_blog_post.html"


class DeleteBlogPostView(AdminRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    This renders a page for confirming the deletion of a blog post,
    which can only be accessed by superusers. This view inherits from
    DeleteView, which handles the deletion of the blogpost.
    """
    model = BlogPost
    template_name = "blog/delete_blog_post.html"
    success_message = "Your blog post was deleted successfully"
    success_url = reverse_lazy('blog')

    # Source success message: StackOverFlow. See README file under 'Sources'.
    def delete(self, request, *args, **kwargs):
        """
        This shows a success message after deletion has succeeded.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteBlogPostView, self).delete(request, *args, **kwargs)


def LikeView(request, pk):
    """
    This view allows users to like/unlike blog posts. After liking/unliking, a
    success message appears.
    """
    blogpost = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    liked = False
    if blogpost.likes.filter(id=request.user.id).exists():
        blogpost.likes.remove(request.user)
        messages.success(request, 'You unliked this blog post')
        liked = False
    else:
        blogpost.likes.add(request.user)
        messages.success(request, 'You liked this blog post')
        liked = True

    return HttpResponseRedirect(reverse('blog_post', args=[str(pk)]))


def BookmarkView(request, pk):
    """
    This view allows users to bookmark blog posts, or remove an existing
    bookmark. After adding/removing a bookmark, a success message appears.
    """
    blogpost = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    bookmarked = False
    if blogpost.bookmarks.filter(id=request.user.id).exists():
        blogpost.bookmarks.remove(request.user)
        messages.success(request, 'You removed this bookmark')
        bookmarked = False
    else:
        blogpost.bookmarks.add(request.user)
        messages.success(request, 'You bookmarked this blog post')
        bookmarked = True

    return HttpResponseRedirect(reverse('blog_post', args=[str(pk)]))


def error(request):
    """
    This renders an error page.
    """
    return render(request, 'blog/error.html')
