from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Comment, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, SearchForm
from django.db.models import Count, Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin


class PostListView(ListView):
    paginate_by = 6
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    category = None

    def get_queryset(self):
        try:
            self.category = get_object_or_404(
                Category, slug=self.kwargs['category_slug'])
            return Post.objects.filter(Q(status='опубликовано')
                                       | Q(status='опубліковано'),
                                       category__in=[self.category])
        except KeyError:
            return Post.objects.filter(
                Q(status='опубликовано')
                | Q(status='опубліковано'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.category:
            context["category"] = self.category
        return context


'''def list_view(request, category_slug=None):
    list_objects = Post.objects.filter(status='опубликовано')
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        list_objects = list_objects.filter(category__in=[category])
    paginator = Paginator(list_objects, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'category': category
    })'''


class PostDetailView(FormMixin, DetailView):
    form_class = CommentForm
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        obj = get_object_or_404(Post,
                                Q(status='опубликовано')
                                | Q(status='опубліковано'),
                                slug=slug,
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        post_categories = self.object.category.values_list('id', flat=True)
        similar = Post.objects.filter(category__in=post_categories).exclude(
            id=self.object.id)
        similar_posts = similar.annotate(
            similarity=Count('category')).order_by('similarity',
                                                   '-publish')[:3]
        context['similar_posts'] = similar_posts
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.post = self.object
        new_comment.save()
        return super().form_valid(form)


'''def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             status='опубликовано')
    comments = post.comments.filter(active=True)
    comment_form = CommentForm()
    post_categories = post.category.values_list('id', flat=True)
    similar = Post.objects.filter(category__in=post_categories).exclude(
        id=post.id)
    similar_posts = similar.annotate(similarity=Count('category')).order_by(
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
        })'''


class SearchView(PostListView):

    def get_queryset(self):
        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            language = self.request.LANGUAGE_CODE
            self.query = search_form.cleaned_data['query']
            search_vector = SearchVector(f'title_{language}',
                                         weight='A') + SearchVector(
                                             f'body_{language}', weight='B')
            search_query = SearchQuery(self.query)
            results = Post.objects.filter(
                Q(status='опубликовано')
                | Q(status='опубліковано')).annotate(
                    rank=SearchRank(search_vector, search_query)).filter(
                        rank__gte=0.1).order_by('-rank')

            return results
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        return context


'''def search(request):
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
    else:
        return redirect('blog:post_list')

    paginator = Paginator(results, 6)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render(request, 'blog/search_results.html', {
        'query': query,
        'results': results
    })'''
