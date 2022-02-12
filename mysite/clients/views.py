from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ClientForm


class ClientFormView(FormView):
    form_class = ClientForm
    template_name = 'clients/form.html'
    success_url = '/'

    def get(self, request, service=None):
        form = self.form_class(initial=self.initial)
        form.set_initial(service)
        return render(request, self.template_name, {
            'form': form,
        })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
