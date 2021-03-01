from django.shortcuts import render


def index(request):
    """Returns home page"""
    return render(request, 'home/index.html')
