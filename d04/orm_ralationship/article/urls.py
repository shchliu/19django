from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('one_to_many/',views.one_to_many_view,name="one_to_many")
]