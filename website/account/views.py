
from distutils.log import error
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('/')     
    return render(request,'account/login.html',{})


def logout_user(request):
    logout(request)
    return redirect('/')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    context={
        'errors':[]
    }    

    if request.method ==  'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        user=User.objects.create(username=username,password=password,email=email)
        if password != password2 :
            complex.get['errors'].append('پسورد و تکرار آن یکی نیست')
            return render(request,'account/register.html',context)
        else:
            login(request,user)
            return redirect('/')    
        
    return render(request,'account/register.html',context)    


