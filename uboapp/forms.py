from django import forms
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }