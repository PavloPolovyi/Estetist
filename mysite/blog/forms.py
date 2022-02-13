from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'name',
            'email',
            'body',
        )
        widgets = {
            'name': forms.TextInput,
            'email': forms.EmailInput,
            'body': forms.Textarea,
        }


class SearchForm(forms.Form):
    query = forms.CharField()
    widgets = {
        'query': forms.TextInput,
    }