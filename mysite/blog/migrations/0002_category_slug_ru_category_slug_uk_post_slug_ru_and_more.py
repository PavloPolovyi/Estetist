# Generated by Django 4.0.2 on 2022-02-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug_ru',
            field=models.SlugField(null=True, verbose_name='URL категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_uk',
            field=models.SlugField(null=True, verbose_name='URL категории'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_ru',
            field=models.SlugField(max_length=250, null=True, unique_for_date='publish', verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_uk',
            field=models.SlugField(max_length=250, null=True, unique_for_date='publish', verbose_name='URL'),
        ),
    ]
