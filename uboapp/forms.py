from django import forms
from .models import Comment, Rating


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



class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        # exclude = ['author', 'updated', 'created', ]
        fields = ['rate']
        widgets = {
            'rate': forms.RadioSelect(
                attrs={'id': 'post-rate', 'required': True, 'placeholder': 'Say something...'}
            ),
        }