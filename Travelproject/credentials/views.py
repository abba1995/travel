from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        psw=request.POST['password']
        user=auth.authenticate(username=uname,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method== 'POST':
         uname = request.POST['username']
         fn = request.POST['first_name']
         ln = request.POST['last_name']
         em = request.POST['email']
         psw = request.POST['password']
         cpsw = request.POST['password1']
         if psw==cpsw:
           if User.objects.filter(username=uname).exists():
                messages.info(request,"User already exist")
                return redirect('register')
           elif User.objects.filter(email=em).exists():
                messages.info(request,"email already exist")
                return redirect('register')
           else:
            user=User.objects.create_user(username=uname,first_name=fn,last_name=ln,email=em,password=psw)
            user.save()
            print("user created")
            return redirect('login')
         else:
              messages.info(request,"password not matching")
              return redirect('register')
         return redirect('/')
    return render(request,"register.html")