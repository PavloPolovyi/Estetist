from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ClientForm
from django.contrib import messages
from django.urls import reverse_lazy
from mysite import settings
import requests


class ClientFormView(FormView):
    form_class = ClientForm
    template_name = 'clients/form.html'
    success_url = reverse_lazy('clients:client_form')
    success_message = 'Спасибо, с вами скоро свяжется наш консультант.'

    def get(self, request, service=None):
        form = self.form_class(initial=self.initial)
        form.set_initial(service)
        return render(
            request, self.template_name, {
                'form': form,
                'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
            })

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                          data=data)
        result = r.json()
        print(result)
        if result['success']:
            form.save()
            response = super().form_valid(form)
            messages.success(self.request, self.success_message)
            return response
