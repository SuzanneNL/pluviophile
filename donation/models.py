import uuid
from django.db import models
from django.contrib.auth.models import User


class Donation(models.Model):
    donation_number = models.CharField(max_length=32, null=False, editable=False)
    donor = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Former user')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_donation_number(self):
        """
        Generates random and unique donation number, using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overrides original save method to set donation number if
        it has not been set already.
        """
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s (€ %s on %s)" % (self.donation_number, self.amount, self.date)
