from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    readonly_fields = ('donation_number', 'date', 'donor', 'donor_full_name')

    fields = ('donation_number', 'date', 'donor', 'donor_full_name')

    ordering = ('-date',)


admin.site.register(Donation, DonationAdmin)
