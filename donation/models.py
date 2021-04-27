import uuid
from django.db import models
from django.contrib.auth.models import User


class Donation(models.Model):
    donation_number = models.CharField(max_length=32, null=False,
                                       editable=False)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    donor_full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

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
        return "%s (by %s on %s)" % (self.donation_number, self.donor,
                                     self.date)
