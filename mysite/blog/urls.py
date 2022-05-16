from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = 'blog'

urlpatterns = [
    path('',
         cache_page(60 * 15)(views.PostListView.as_view()),
         name='post_list'),
    path('tag/<slug:category_slug>',
         views.PostListView.as_view(),
         name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>',
         views.PostDetailView.as_view(),
         name='post_detail'),
    path('comment/add/<int:post_id>',
         views.CommentFormView.as_view(),
         name='submit_comment_form')
]
