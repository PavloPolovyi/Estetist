from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):

    STATUS_CHOICES = (
        ('черновик', 'Чeрновик'),
        ('опубликовано', 'Опубликовано'),
    )

    title = models.CharField('Заголовок', max_length=250)
    image = models.ImageField('Изображение', upload_to='post_images/')
    slug = models.SlugField('URL', max_length=250, unique_for_date='publish')
    body = models.TextField("Текст поста")
    publish = models.DateTimeField('Дата публикации', default=timezone.now)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования',
                                   auto_now=True)
    status = models.CharField('Статус поста',
                              max_length=12,
                              choices=STATUS_CHOICES,
                              default='черновик')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish', )
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

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
                             verbose_name='Пост',
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField('Имя', max_length=80)
    email = models.EmailField()
    body = models.TextField('Текст комментария')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата последнего редактирования',
                                   auto_now=True)
    active = models.BooleanField('Активный', default=True)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
