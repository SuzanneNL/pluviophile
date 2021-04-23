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


class ForumView(LoginRequiredMixin, SortableListView):
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
        context = super(ForumView, self).get_context_data(**kwargs)
        context['threads_count'] = Thread.objects.count()
        return context


class ThreadView(LoginRequiredMixin, DetailView):
    model = Thread
    template_name = "forum/thread.html"
    ordering = ['date_created']

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        comments = Paginator(self.object.comments.all().order_by(
                             'date_created'), 5)
        context['all_threads_on_forum'] = Thread.objects.all()
        context['all_comments_on_forum'] = Comment.objects.all()
        context['comments'] = comments.get_page(page)
        context['comments_count'] = self.object.comments.count()
        return context


class StartThreadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was created successfully"
    template_name = "forum/start_thread.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditThreadView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was updated successfully"
    template_name = "forum/edit_thread.html"

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')


class DeleteThreadView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Thread
    template_name = "forum/delete_thread.html"
    success_message = "Your thread was deleted successfully"
    success_url = reverse_lazy('forum')

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteThreadView, self).delete(request, *args, **kwargs)


class AddCommentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    template_name = "forum/add_comment.html"
    success_message = "Your comment was added successfully"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('thread', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.thread_id = self.kwargs['pk']
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    template_name = "forum/edit_comment.html"
    success_message = "Your comment was updated successfully"
    form_class = CommentForm

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Comment
    success_message = "Your comment was deleted successfully"
    template_name = "forum/delete_comment.html"

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteCommentView, self).delete(request, *args, **kwargs)


def error(request):
    return render(request, 'forum/error.html')
