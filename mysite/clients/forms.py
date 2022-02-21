from django import forms
from .models import Client
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'email', 'phone', 'service', 'message')
        widgets = {
            'name': forms.TextInput,
            'email': forms.EmailInput,
            'phone': PhoneNumberPrefixWidget(initial='UA'),
            'service': forms.Select,
            'message': forms.Textarea,
        }
        labels = {'name': _('Ваше имя'), 'message': _('Ваше сообщение')}

    def set_initial(self, value):
        if value == 'base':
            self.initial['service'] = _('Пакет Базовый подбор')
        elif value == 'plus':
            self.initial['service'] = _('Пакет Подбор Плюс')
        elif value == 'full':
            self.initial['service'] = _('Пакет Все включено')
        else:
            self.initial['service'] = None
