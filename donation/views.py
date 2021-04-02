from django.shortcuts import render
from .forms import DonationForm


def donate(request):
    return render(request, 'donation/donate.html')


def charge(request):
    donation_form = DonationForm()
    template = 'donation/charge.html'
    context = {
        'donation_form': donation_form,
    }
    return render(request, template, context)


def donation_success(request):
    return render(request, 'donation/donation_success.html')
