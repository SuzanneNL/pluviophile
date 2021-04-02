from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    readonly_fields = ('donation_number', 'date', 'amount', 'donor')

    fields = ('donation_number', 'amount', 'donor', 'date')

    ordering = ('-date',)


admin.site.register(Donation, DonationAdmin)
