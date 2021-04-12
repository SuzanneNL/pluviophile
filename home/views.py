from django.shortcuts import render


def index(request):
    """Returns home page"""
    return render(request, 'home/index.html')


def rain(request):
    """Returns rain page. Allows users to go back to previous page"""
    template = 'home/rain.html'
    context = {
        'goback': request.META.get('HTTP_REFERER')
    }
    return render(request, template, context)
