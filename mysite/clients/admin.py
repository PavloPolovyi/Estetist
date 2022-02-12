from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'service',
        'application_date',
        'active',
    )
    list_filter = (
        'application_date',
        'active',
    )
    date_hierarchy = 'application_date'
    search_fields = (
        'name',
        'message',
    )
    list_editable = ('active', )
