from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
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
    fields = "__all__"
