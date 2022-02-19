from django.urls import path
from .views import client_form_view

app_name = 'clients'

urlpatterns = [
    path('', client_form_view, name="client_form"),
    path('<str:service>', client_form_view, name="client_form_params")
]
