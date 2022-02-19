from django.shortcuts import render, redirect
from .forms import ClientForm
from django.contrib import messages
from django.urls import reverse_lazy
from mysite import settings
import requests

success_message = 'Спасибо, с вами скоро свяжется наш консультант.'
error_message = 'Заполните форму корректными данными.'


def client_form_view(request, service=None):
    form = ClientForm()
    form.set_initial(service)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:
                form.save()
                messages.success(request, success_message)
                return redirect('clients:client_form')
        else:
            messages.error(request, error_message)
    return render(request, 'clients/form.html', {
        'form': form,
        'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
    })
