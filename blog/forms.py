from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
    Form for creating/editing blog posts. Please see README file under
    'Features left to implement' for planned changes.
    """
    class Meta:
        model = BlogPost
        fields = (
            'title',
            'author',
            'image_1',
            'image_1_description',
            'body_part_1',
            'image_2',
            'image_2_description',
            'body_part_2',
            'image_3',
            'image_3_description',
            'body_part_3',
            'source_comment',
            )
