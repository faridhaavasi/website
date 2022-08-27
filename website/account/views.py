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