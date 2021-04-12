from django.shortcuts import render


def index(request):
    """Returns home page"""
    return render(request, 'home/index.html')


def rain(request):
    """Returns rain page"""
    return render(request, 'home/rain.html')
