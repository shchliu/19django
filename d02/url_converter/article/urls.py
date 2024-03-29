from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.article),
    # \w 0-9 a-z A-Z
    # | 或
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/', views.article_list),
    path('list/<cate:categories>/', views.article_list, name='list')
]
