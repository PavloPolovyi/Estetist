from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q, Prefetch
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


class PostListView(ListView):
    queryset = Post.objects.filter(
        Q(status='опубликовано') | Q(status='опубліковано'))
    paginate_by = 6
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    category = None
    query = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.query = self.request.GET.get('query', None)
        self.category = self.kwargs.get('category_slug', None)
        if self.query:
            language = self.request.LANGUAGE_CODE
            search_vector = SearchVector(f'title_{language}',
                                         weight='A') + SearchVector(
                                             f'body_{language}', weight='B')
            search_query = SearchQuery(self.query)
            queryset = queryset.annotate(
                rank=SearchRank(search_vector, search_query)).filter(
                    rank__gte=0.1).order_by('-rank')
        if self.category:
            queryset = queryset.filter(category__slug__in=[self.category])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context['query'] = self.query
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.filter(
        Q(status='опубликовано') | Q(status='опубліковано'))
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
            Prefetch('comments', queryset=Comment.objects.filter(active=True)))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class CommentFormView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        self.post = Post.objects.get(id=self.kwargs.get('post_id'))
        form.instance.post = self.post
        self.request.session['has_commented'] = True
        return super().form_valid(form)

    def get_success_url(self):
        return self.post.get_absolute_url()
