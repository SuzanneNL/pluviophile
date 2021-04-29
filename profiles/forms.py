from django import forms
from .models import Profile
import datetime


class DatePicker(forms.DateInput):
    """
    Allows users to select their date of birth with a datepicker.
    """
    input_type = 'date'


class ProfileForm(forms.ModelForm):
    """
    Form for editing the profile.
    """
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'country', 'biography', 'avatar')
        widgets = {'date_of_birth': DatePicker}

    # Source for forbidding dates in future: StackOverFlow.
    # See README file under 'Sources'.
    def clean_date_of_birth(self):
        """
        This makes sure only dates in the past are accepted as date of birth.
        It gives an error message when a user enters a date in the future/
        present.
        """
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth:
            if date_of_birth >= datetime.date.today():
                raise forms.ValidationError("Select a date in the past")
            return date_of_birth
