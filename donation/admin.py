from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    readonly_fields = (
                'donation_number',
                'date',
                'donor',
                'donor_full_name',
                'stripe_pid'
                )

    fields = (
        'donation_number',
        'date',
        'donor',
        'donor_full_name',
        'stripe_pid'
        )

    ordering = ('-date',)


admin.site.register(Donation, DonationAdmin)
