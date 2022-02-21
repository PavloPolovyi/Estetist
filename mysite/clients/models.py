from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Client(models.Model):

    SERVICE_CHOICES = (
        (_('Пакет Базовый подбор'), _('Пакет Базовый подбор')),
        (_('Пакет Подбор Плюс'), _('Пакет Подбор Плюс')),
        (_('Пакет Все включено'), _('Пакет Все включено')),
    )

    email = models.EmailField(null=False, blank=False, unique=True)
    name = models.CharField(_('Имя'), max_length=80, blank=False)
    phone = PhoneNumberField(_('Номер телефона'),
                             null=False,
                             blank=False,
                             unique=True)
    service = models.CharField(_('Услуга'),
                               choices=SERVICE_CHOICES,
                               max_length=20)
    message = models.TextField(_('Сообщение'))
    application_date = models.DateTimeField(_('Дата заполнения формы'),
                                            auto_now_add=True)
    active = models.BooleanField(_('Активный'), default=True)

    class Meta:
        ordering = ('-application_date', 'name')
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.application_date}'