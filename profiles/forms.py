from django import forms
from .models import Profile


class DatePicker(forms.DateInput):
    input_type = 'date'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'country', 'biography', 'avatar')
        widgets = {'date_of_birth': DatePicker}
