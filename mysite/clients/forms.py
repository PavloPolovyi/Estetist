from django import forms
from .models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'service', 'message')
        widgets = {
            'name': forms.TextInput,
            'email': forms.EmailInput,
            'phone': forms.TextInput,
            'service': forms.Select,
            'message': forms.Textarea,
        }

    def set_initial(self, value):
        if value == 'base':
            self.initial['service'] = 'Пакет Базовый подбор'
        elif value == 'plus':
            self.initial['service'] = 'Пакет Подбор Плюс'
        elif value == 'full':
            self.initial['service'] = 'Пакет Все включено'
        else:
            self.initial['service'] = None
