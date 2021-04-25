from django.shortcuts import render


def index(request):
    """Returns home page"""
    template = 'home/index.html'
    return render(request, template)


def rain(request):
    """Returns rain page. Allows users to go back to previous page"""
    template = 'home/rain.html'
    goback = request.META.get('HTTP_REFERER')
    context = {
        'goback': goback,
    }
    return render(request, template, context)
