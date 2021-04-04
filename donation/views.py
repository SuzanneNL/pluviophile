from django.shortcuts import render
from .forms import DonationForm
from django.conf import settings
import stripe


def donate(request):
    return render(request, 'donation/donate.html')


def charge(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=500,
        currency=settings.STRIPE_CURRENCY,
    )

    donation_form = DonationForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'donation/charge.html'
    context = {
        'donation_form': donation_form,
        'stripe_public_key': 'stripe_public_key',
        'client_secret': 'intent.client_secret',
    }
    return render(request, template, context)


def donation_success(request):
    return render(request, 'donation/donation_success.html')
