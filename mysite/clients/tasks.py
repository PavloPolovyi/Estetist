from celery import shared_task
from django.core.mail import send_mail
from .models import Client


@shared_task
def admin_notification(client_id):
    client = Client.objects.get(id=client_id)
    subject = f'Новый клиент Estetist - {client.name}'
    message = f'''Новый клиент заполнил форму на сайте - {client.name}.\n\n 
              Номер телефона клиента: {client.phone}\n
              E-mail клиента: {client.email}\n
              Выбранный сервис: {client.service}\n
              Сообщение клиента: {client.message}
    '''
    mail_sent = send_mail(subject, message, 'admin@estetist.com',
                          ['your.estetist@gmail.com'])
    return mail_sent
