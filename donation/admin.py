from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    """
    This makes the fields uneditable in the admin panel. Donations are
    ordered from new to old.
    """
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
