"""Post forms"""

# Django 
from django import forms

# Models
from posts.models import Posts


class PostForm(forms.ModelForm):
    """Post model forms"""

    class Meta:
        """Form setting"""

        model = Posts
        fields = ('user', 'profile', 'title', 'photo')