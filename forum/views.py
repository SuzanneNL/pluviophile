from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import ThreadForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Thread, Comment


class ForumView(LoginRequiredMixin, ListView):
    model = Thread
    template_name = "forum/forum.html"
    paginate_by = 5


class ThreadView(LoginRequiredMixin, DetailView):
    model = Thread
    template_name = "forum/thread.html"

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        comments = Paginator(self.object.comments.all(), 5)
        context['comments'] = comments.get_page(page)
        context['comments_number'] = self.object.comments.count()
        return context


class StartThreadView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "forum/start_thread.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditThreadView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = "forum/edit_thread.html"

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')


class DeleteThreadView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    template_name = "forum/delete_thread.html"
    success_url = reverse_lazy('forum')

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "forum/add_comment.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('thread', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.thread_id = self.kwargs['pk']
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = "forum/edit_comment.html"
    form_class = CommentForm

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')


class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "forum/delete_comment.html"

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        return False

    def handle_no_permission(self):
        return redirect('error')


def error(request):
    return render(request, 'forum/error.html')
