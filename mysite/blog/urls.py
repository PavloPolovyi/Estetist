from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.list_view, name='post_list'),
    path('tag/<int:tag_id>', views.list_view, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>',
         views.post_detail,
         name='post_detail'),
    path('search/', views.search, name='search'),
]
