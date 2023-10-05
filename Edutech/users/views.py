
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request, 'index.html')


def register(request):
    if (request.method=='POST'):
        u = request.POST['u']
        f= request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        c = request.POST['c']
        if p==c:
            user=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
            user.save()
            return home(request)


    return render(request,'register.html')
def user_login(request):
    if(request.method=='POST'):
        u= request.POST['u']
        p= request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"invalid credentials")

    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return home(request)

