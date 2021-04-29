from django import forms
from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    """
    Form for creating/editing threads.
    """
    class Meta:
        model = Thread
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    """
    Form for creating/editing comments.
    """
    class Meta:
        model = Comment
        fields = ('post',)
