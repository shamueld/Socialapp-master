from .models import Post, Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('message',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('message', 'group')
