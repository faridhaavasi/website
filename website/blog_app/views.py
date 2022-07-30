
from turtle import title
from django.shortcuts import render
from . models import Article,Abute,Ticket
# Create your views here.
def home(request):
    return render(request,'home.html')

def Atricle_list(request):
    articles=Article.objects.all()
    return render(request,'article_list.html',context={'articles':articles})

def detail(request,id):
    article=Article.objects.get(id=id)
    article.views+=1
    article.save()
    return render(request,'detail.html',context={'article':article})
def abute_me(request):
    abute=Abute.objects.all()
    return render(request,'abute.html',context={'Abute':abute})

def call(request):
    if request.method=='POST':
        title=request.POST.get('title')
        email=request.POST.get('email')
        description=request.POST.get('description')
        Ticket.objects.create(title=title,email=email,description=description)

    
    return render(request,'call.html')    