from django import template
from ..models import Post, Category
from django.db.models import Count, Q
from ..forms import SearchForm

register = template.Library()


@register.simple_tag
def show_latest_posts(number=5):
    return Post.objects.all().filter(
        Q(status='опубликовано')
        | Q(status='опубліковано')).order_by('-publish')[:number]


@register.simple_tag
def get_most_commented_posts(number=5):
    return Post.objects.filter(
        Q(status='опубликовано')
        | Q(status='опубліковано'), ).annotate(total_comments=Count(
            'comments')).order_by('-total_comments')[:number]


@register.simple_tag
def categories():
    return Category.objects.all()


@register.inclusion_tag('blog/search.html')
def search():
    search_form = SearchForm()
    return {'search_form': search_form}
