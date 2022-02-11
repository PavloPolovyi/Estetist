from django import template
from ..models import Post
from django.db.models import Count
from taggit.models import Tag

register = template.Library()


@register.simple_tag
def show_latest_posts(number=5):
    return Post.objects.all().filter(
        status='опубликовано').order_by('-publish')[:number]


@register.simple_tag
def get_most_commented_posts(number=5):
    return Post.objects.all().filter(status='опубликовано').annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:number]


@register.simple_tag
def categories():
    return Tag.objects.all()
