# Generated by Django 4.0.2 on 2022-02-21 17:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название категории')),
                ('name_ru', models.CharField(max_length=120, null=True, verbose_name='Название категории')),
                ('name_uk', models.CharField(max_length=120, null=True, verbose_name='Название категории')),
                ('slug', models.SlugField(verbose_name='URL категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Заголовок')),
                ('title_uk', models.CharField(max_length=250, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='post_images/', verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish', verbose_name='URL')),
                ('body', models.TextField(verbose_name='Текст поста')),
                ('body_ru', models.TextField(null=True, verbose_name='Текст поста')),
                ('body_uk', models.TextField(null=True, verbose_name='Текст поста')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')),
                ('status', models.CharField(choices=[('черновик', 'Чeрновик'), ('опубликовано', 'Опубликовано')], default='черновик', max_length=12, verbose_name='Статус поста')),
                ('category', models.ManyToManyField(related_name='posts', to='blog.Category')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('created',),
            },
        ),
    ]
