# Source: This app was largely influenced by tutorials
# from CoreyMS and John Elder. See README file under 'Sources'.

from django.shortcuts import render, redirect
from sortable_listview import SortableListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import ThreadForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Thread, Comment


# Source SortableListView: django-sortable-listview documentation
# See README file under 'Sources'
class ForumView(LoginRequiredMixin, SortableListView):
    """
    This renders a list of all threads. Login is required. It is paginated, and
    there are multiple sorting options.
    """
    model = Thread
    template_name = "forum/forum.html"
    paginate_by = 5
    allowed_sort_fields = {'date_created': {'default_direction': '-',
                                            'verbose_name': 'Date'},
                           'title': {'default_direction': '',
                                     'verbose_name': 'Title'},
                           }
    default_sort_field = 'date_created'

    def get_context_data(self, **kwargs):
        """
        This counts the number of threads, and it is passed to the
        template as context.
        """
        context = super(ForumView, self).get_context_data(**kwargs)
        context['threads_count'] = Thread.objects.count()
        return context


class ThreadView(LoginRequiredMixin, DetailView):
    """
    This renders a single thread. Login is required.
    """
    model = Thread
    template_name = "forum/thread.html"
    ordering = ['date_created']

    # Source for pagination: StackOverFlow. See README file under 'Sources'
    def get_context_data(self, **kwargs):
        """
        This is where pagination for comments is arranged. It also passes
        the number of threads and comments on the forum as context, which is
        needed on the template.
        """
        context = super(ThreadView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        comments = Paginator(self.object.comments.all().order_by(
                             '-date_created'), 5)
        context['all_threads_on_forum'] = Thread.objects.all()
        context['all_comments_on_forum'] = Comment.objects.all()
        context['comments'] = comments.get_page(page)
        context['comments_count'] = self.object.comments.count()
        return context


class StartThreadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    This renders a page with a form for adding a thread, which can only be
    accessed by registered users. This view inherits from CreateView, which
    handles the creation of the thread. After creation, a success message
    appears.
    """
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was created successfully"
    template_name = "forum/start_thread.html"

    def form_valid(self, form):
        """
        This overrides form_valid() to add the logged in user as the creator of
        the thread.
        """
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditThreadView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, UpdateView):
    """
    This renders a page with a form for editing a thread, which can only be
    accessed by registered users. This view inherits from UpdateView, which
    handles the updating of the thread. After the update, a success message
    appears.
    """
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was updated successfully"
    template_name = "forum/edit_thread.html"

    def test_func(self):
        """
        This makes sure only the creator of the thread and superusers can edit
        the thread.
        """
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    # Source for redirecting: StackOverFlow. See README file under 'Sources'.
    def handle_no_permission(self):
        """
        Other users get redirected to the error page, when trying to access the
        edit page.
        """
        return redirect('error')


class DeleteThreadView(LoginRequiredMixin, UserPassesTestMixin,
                       SuccessMessageMixin, DeleteView):
    """
    This renders a page for confirming the deletion of a thread. This view
    inherits from DeleteView, which handles the deletion of the thread.
    """
    model = Thread
    template_name = "forum/delete_thread.html"
    success_message = "Your thread was deleted successfully"
    success_url = reverse_lazy('forum')

    def test_func(self):
        """
        This makes sure only the creator and superusers can delete a thread.
        """
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        """
        Other users get redirected to the error page, when trying to access the
        confirm deletion page.
        """
        return redirect('error')

    # Source success message: StackOverFlow. See README file under 'Sources'.
    def delete(self, request, *args, **kwargs):
        """
        This shows a success message after deletion has succeeded.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteThreadView, self).delete(request, *args, **kwargs)


class AddCommentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    This renders a page with a form for adding a comment, which can only be
    accessed by registered users. This view inherits from CreateView, which
    handles the creation of a comment. After creation, a success message
    appears.
    """
    model = Comment
    template_name = "forum/add_comment.html"
    success_message = "Your comment was added successfully"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('thread', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        """
        This overrides form_valid() to add the logged in user as the creator of
        the comment.
        """
        form.instance.thread_id = self.kwargs['pk']
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditCommentView(LoginRequiredMixin, UserPassesTestMixin,
                      SuccessMessageMixin, UpdateView):
    """
    This renders a page with a form for editing a comment, which can only be
    accessed by registered users. This view inherits from UpdateView, which
    handles the updating of the comment. After the update, a success message
    appears.
    """
    model = Comment
    template_name = "forum/edit_comment.html"
    success_message = "Your comment was updated successfully"
    form_class = CommentForm

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    def test_func(self):
        """
        This makes sure only the creator of the comment and superusers can edit
        the comment.
        """
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        """
        Other users get redirected to the error page, when trying to access the
        edit page.
        """
        return redirect('error')


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin,
                        SuccessMessageMixin, DeleteView):
    """
    This renders a page for confirming the deletion of a comment. This view
    inherits from DeleteView, which handles the deletion of the comment.
    """
    model = Comment
    success_message = "Your comment was deleted successfully"
    template_name = "forum/delete_comment.html"

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    def test_func(self):
        """
        This makes sure only the creator of the comment and superusers can
        delete the comment.
        """
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        """
        Other users get redirected to the error page, when trying to access the
        confirm deletion page.
        """
        return redirect('error')

    def delete(self, request, *args, **kwargs):
        """
        This shows a success message after deletion has succeeded.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteCommentView, self).delete(request, *args, **kwargs)


def error(request):
    """
    This renders an error page.
    """
    return render(request, 'forum/error.html')
