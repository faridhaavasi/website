
from django.shortcuts import render
from . models import Article
# Create your views here.
def home(request):
    return render(request,'home.html')

def Atricle_list(request):
    articles=Article.objects.all()
    return render(request,'article_list.html',context={'articles':articles})

