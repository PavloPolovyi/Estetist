from django.urls import path
from .views import ClientFromView

app_name = 'clients'

urlpatterns = [
    path('', ClientFromView.as_view(), name="client_form"),
    path('<str:service>', ClientFromView.as_view(), name="client_form_params")
]
