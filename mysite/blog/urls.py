from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', views.list_view, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # path('tag/<slug:category_slug>', views.list_view, name='post_list_by_tag'),
    path('tag/<slug:category_slug>',
         views.PostListView.as_view(),
         name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>',
         views.PostDetailView.as_view(),
         name='post_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]
