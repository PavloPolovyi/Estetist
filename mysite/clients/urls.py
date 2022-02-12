from django.urls import path
from .views import ClientFormView

app_name = 'clients'

urlpatterns = [
    path('', ClientFormView.as_view(), name="client_form"),
    path('<str:service>', ClientFormView.as_view(), name="client_form_params")
]
