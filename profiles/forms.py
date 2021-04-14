from django import forms
from .models import Profile
import datetime


class DatePicker(forms.DateInput):
    input_type = 'date'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'country', 'biography', 'avatar')
        widgets = {'date_of_birth': DatePicker}

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth >= datetime.date.today():
            raise forms.ValidationError("Select a date in the past")
        return date_of_birth
