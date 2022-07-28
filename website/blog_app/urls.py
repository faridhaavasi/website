from urllib.parse import urlparse
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('article_list',views.Atricle_list)
]
