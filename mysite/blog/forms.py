from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _


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

        labels = {'body': _('Ваш комментарий')}


class SearchForm(forms.Form):
    query = forms.CharField(label='')

    class Meta:
        widgets = {
            'query': forms.TextInput,
        }
