from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass0=request.POST['pass0']
        pass1=request.POST['pass1']
        if pass0==pass1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already in use")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pass0)
                user.save()
                return redirect('/')
        else:
            messages.info(request,"Password not matched")
            return redirect('register')

    return render(request,"register.html ")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pass0=request.POST['pass0']
        user=auth.authenticate(username=username,password=pass0)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
