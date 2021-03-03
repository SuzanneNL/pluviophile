from django.shortcuts import render
from django.views.generic import ListView
from .models import Thread


# def forum(request):
#     return render(request, 'forum/forum.html', {})

class Forum(ListView):
    model = Thread
    template_name = "forum/forum.html"
