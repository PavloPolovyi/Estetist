from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from .forms import CommentForm, SearchForm
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def list_view(request, tag_id=None):
    list_objects = Post.objects.all().filter(status='опубликовано')
    tag = None
    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        list_objects = list_objects.filter(tags__in=[tag])
    paginator = Paginator(list_objects, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_list.html', {'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             status='опубликовано')
    comments = post.comments.all().filter(active=True)
    comment_form = CommentForm()
    new_comment = None
    post_tags = post.tags.values_list('id', flat=True)
    similar = Post.objects.filter(tags__in=post_tags).exclude(id=post.id)
    similar_posts = similar.annotate(similarity=Count('tags')).order_by(
        'similarity', '-publish')[:3]
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url())
    return render(
        request, 'blog/blog_detail.html', {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'similar_posts': similar_posts,
        })


def search(request):
    query = None
    results = []
    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + SearchVector(
                'body', weight='B')
            search_query = SearchQuery(query)
            results = Post.objects.filter(status='опубликовано').annotate(
                rank=SearchRank(search_vector, search_query)).filter(
                    rank__gte=0.1).order_by('-rank')

    paginator = Paginator(results, 6)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        results = paginator.page(paginator.num_pages)
    return render(request, 'blog/search_results.html', {
        'query': query,
        'results': results
    })
