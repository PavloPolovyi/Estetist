from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Название категории'), max_length=120)
    slug = models.SlugField(_("URL категории"))

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_list_by_tag', args=[self.slug])


class Post(models.Model):

    STATUS_CHOICES = (
        (_('черновик'), _('Чeрновик')),
        (_('опубликовано'), _('Опубликовано')),
    )

    title = models.CharField(_('Заголовок'), max_length=250)
    image = models.ImageField(_('Изображение'), upload_to='post_images/')
    slug = models.SlugField('URL', max_length=250, unique_for_date='publish')
    body = models.TextField(_("Текст поста"))
    publish = models.DateTimeField(_('Дата публикации'), default=timezone.now)
    created = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated = models.DateTimeField(_('Дата последнего редактирования'),
                                   auto_now=True)
    status = models.CharField(_('Статус поста'),
                              max_length=12,
                              choices=STATUS_CHOICES,
                              default=_('черновик'))
    category = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ('-publish', )
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                           self.publish.year, self.publish.month,
                           self.publish.day, self.slug
                       ])


class Comment(models.Model):

    post = models.ForeignKey(Post,
                             verbose_name=_('Пост'),
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(_('Имя'), max_length=80)
    email = models.EmailField()
    body = models.TextField(_('Текст комментария'))
    created = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated = models.DateTimeField(_('Дата последнего редактирования'),
                                   auto_now=True)
    active = models.BooleanField(_('Активный'), default=True)

    class Meta:
        ordering = ('created', )
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def __str__(self):
        return f'Комментарий сделанный {self.name} к публикации {self.post}'
