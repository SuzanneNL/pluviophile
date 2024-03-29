from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    """
    Form for creation of a donation.
    """
    class Meta:
        """
        The donor is the logged in user. That field is hidden.
        """
        model = Donation
        fields = ('donor_full_name', 'donor', 'email')

        widgets = {'donor': forms.TextInput(attrs={
            'class': 'form-control',
            'value': '',
            'id': 'donor',
            'type': 'hidden',
            })}

    def __init__(self, *args, **kwargs):
        """
        Add classes, remove auto-generated labels and set autofocus
        on first field.
        """
        super().__init__(*args, **kwargs)

        self.fields['donor_full_name'].widget.attrs['autofocus'] = True
        self.fields['donor_full_name'].label = "Cardholder Name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
