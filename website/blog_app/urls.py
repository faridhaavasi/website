from urllib.parse import urlparse
from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.home,name='home'),
    path('article_list',views.Atricle_list,name='Atricle_list'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('abute',views.abute_me,name='abute_me'),
    path('call',views.call,name='call')
]
