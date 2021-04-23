from django.shortcuts import render, redirect
from blog.models import BlogPost
from django.shortcuts import get_object_or_404


def index(request):
    """Returns home page"""
    blogpost = get_object_or_404(BlogPost, pk=1)
    template = 'home/index.html'
    context = {
        'blogpost': blogpost,
    }
    return render(request, template, context)


def rain(request):
    """Returns rain page. Allows users to go back to previous page"""
    template = 'home/rain.html'
    goback = request.META.get('HTTP_REFERER')
    if not goback:
        return redirect('home')
    context = {
        'goback': goback,
    }
    return render(request, template, context)
