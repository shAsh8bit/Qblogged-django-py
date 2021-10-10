from django.core import validators
from django import forms
from .models import Blog,DiscussionA

class Update_blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['head','body']


class Post_answers(forms.ModelForm):
    class Meta:
        model = DiscussionA
        fields=['body']        