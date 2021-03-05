from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Thread


class ForumView(LoginRequiredMixin, ListView):
    model = Thread
    template_name = "forum/forum.html"


class ThreadView(LoginRequiredMixin, DetailView):
    model = Thread
    template_name = "forum/thread.html"


class StartThreadView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = "forum/start_thread.html"
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditThreadView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    template_name = "forum/edit_thread.html"
    fields = ['title', 'description']

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


def error(request):
    return render(request, 'forum/error.html')
