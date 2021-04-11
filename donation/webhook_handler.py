from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from donation.models import Donation
from django.contrib.auth.models import User

import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, donation):
        """Send the user a confirmation email"""
        donor_email = donation.email
        subject = render_to_string(
            'donation/confirmation_emails/confirmation_email_subject.txt',
            {'donation': donation})
        body = render_to_string(
            'donation/confirmation_emails/confirmation_email_body.txt',
            {'donation': donation, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [donor_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        billing_details = intent.charges.data[0].billing_details

        # Clean data in the shipping details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        user_email = intent.charges.data[0].billing_details.email
        if self.request.user != 'AnonymousUser':
            user = User.objects.get(email=user_email)

        donation_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                donation = Donation.objects.get(
                    donor=user,
                    donor_full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    stripe_pid=pid,
                )
                donation_exists = True
                break

            except Donation.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if donation_exists:
            self._send_confirmation_email(donation)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified donation already in database',
                status=200)
        else:
            donation = None
            try:
                donation = Donation.objects.create(
                        donor=user,
                        donor_full_name=billing_details.name,
                        email=billing_details.email,
                        stripe_pid=pid,
                    )
            except Exception as e:
                if donation:
                    donation.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(donation)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created donation in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
