from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_,logout
from django.contrib import  messages
from .models import Auth



def login_view(request):
    # print('erwsfrgrh')
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login_(request,user)
            return redirect('artical')
        else:
            messages.error(request,'Your username and password are wrong')
    return render(request,'login.html')

    
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        conformation = request.POST['conformation']

        if password != conformation:
            return redirect('register')
        else:
            user=Auth.objects.create_user(username=username,password=password)
            user.save()
            return redirect('login')
    return render(request,'register.html')


def logout_view(request):
    logout(request)
    return redirect('login')
