
from django.shortcuts import render
from . models import Article
# Create your views here.
def home(request):
    return render(request,'home.html')

def Atricle_list(request):
    articles=Article.objects.all()
    return render(request,'article_list.html',context={'articles':articles})

def detail(request,id):
    article=Article.objects.get(id=id)
    article.views=+1
    article.save()
    return render(request,'detail.html',context={'article':article})
    