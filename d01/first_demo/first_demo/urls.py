"""first_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
# from book.views import book,movie
from book import views


def index(request):
    return HttpResponse("豆瓣首页")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book/', views.book),
    path('movie/', views.movie),
    path('book/detail/<book_id>/<category_id>/', views.book_detail),
    path('author/', views.author_detail)

]
