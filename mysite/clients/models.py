from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):

    SERVICE_CHOICES = (
        ('Пакет Базовый подбор', 'Пакет Базовый подбор'),
        ('Пакет Подбор Плюс', 'Пакет Подбор Плюс'),
        ('Пакет Все включено', 'Пакет Все включено'),
    )

    email = models.EmailField(null=False, blank=False, unique=True)
    name = models.CharField('Имя', max_length=80, blank=False)
    phone = PhoneNumberField('Номер телефона',
                             null=False,
                             blank=False,
                             unique=True)
    service = models.CharField('Услуга',
                               choices=SERVICE_CHOICES,
                               max_length=20)
    message = models.TextField('Сообщение')
    application_date = models.DateTimeField('Дата заполнения формы',
                                            auto_now_add=True)
    active = models.BooleanField('Активный', default=True)

    class Meta:
        ordering = ('-application_date', 'name')
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'