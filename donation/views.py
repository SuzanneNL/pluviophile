from django.shortcuts import render


def donate(request):
    return render(request, 'donation/donate.html')


def charge(request):
    return render(request, 'donation/charge.html')


def donation_success(request):
    return render(request, 'donation/donation_success.html')
