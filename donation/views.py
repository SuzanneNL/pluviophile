from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DonationForm
from .models import Donation
from django.conf import settings
import stripe


@login_required
def donate(request):
    return render(request, 'donation/donate.html')


@login_required
def charge(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form_data = {
            'donor': request.user,
            'donor_full_name': request.POST['donor_full_name'],
            'email': request.POST['email'],
        }
        donation_form = DonationForm(form_data)
        if donation_form.is_valid():
            donation = donation_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            donation.stripe_pid = pid
            donation.save()
            return redirect(reverse('donation_success',
                                    args=[donation.donation_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
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
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def donation_success(request, donation_number):
    donation = get_object_or_404(Donation, donation_number=donation_number)
    if request.user == donation.donor:
        messages.success(request, 'Your donation was successfully processed!')
        template = 'donation/donation_success.html'
        context = {
            'donation': donation,
        }

        return render(request, template, context)
    else:
        return redirect('error')


def error(request):
    return render(request, 'donation/error.html')
