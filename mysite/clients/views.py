import requests
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from mysite import settings
from .tasks import admin_notification
from .forms import ClientForm


class ClientFromView(FormView):
    form_class = ClientForm
    template_name = 'clients/form.html'
    success_url = reverse_lazy('clients:client_form')
    success_message = _('Спасибо, с вами скоро свяжется наш консультант.')
    error_message = _('Заполните форму корректными данными.')
    error_message_captcha = _(
        'Извините, что то пошло не так. Попробуйте еще раз.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recaptcha_site_key'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
        form = self.form_class()
        form.set_initial(self.kwargs.get('service', None))
        context['form'] = form
        return context

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                          data=data)
        result = r.json()
        if result['success']:
            new_client = form.save()
            admin_notification.delay(new_client.id)
            messages.success(self.request, self.success_message)
            return super().form_valid(form)
        else:
            messages.error(self.request, self.error_message_captcha)
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)
