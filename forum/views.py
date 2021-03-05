from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Thread


class ForumView(ListView):
    model = Thread
    template_name = "forum/forum.html"


class ThreadView(DetailView):
    model = Thread
    template_name = "forum/thread.html"


class StartThreadView(CreateView):
    model = Thread
    template_name = "forum/start_thread.html"
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditThreadView(UpdateView):
    model = Thread
    template_name = "forum/edit_thread.html"
    fields = ['title', 'description']


class DeleteThreadView(DeleteView):
    model = Thread
    template_name = "forum/delete_thread.html"
    success_url = reverse_lazy('forum')
