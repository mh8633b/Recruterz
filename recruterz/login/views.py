from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.





def register(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['username']
        password1 = request.POST['password']

        # user = User.objects.create_user(username = uname, password=password1, first_name=fname, last_name=lname)
        if uname == '':
            print("please enter a username")
            messages.info(request, "Please Enter a Username")
            return redirect("register")

        elif User.objects.filter(username=uname).exists():
            print("username already exists")
            messages.info(request, "Username Already Exists")
            return redirect("register")
        elif len(password1) < 8:
            print("password should be grater than 8")
            messages.info(request, "password should be grater than 8")
            return redirect("register")

        else:
            user = User.objects.create_user(
                username=uname, password=password1,email=email,  first_name=fname,last_name=lname)
            user.save()
            print("User Created")
            return redirect("/")
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        # fname = request.POST['firstname']
        # lname = request.POST['lastname']
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user is None:
            print("password should be grater than 8")
            messages.info(request, "Invalid Credentials")
            return redirect("login")
        else:
            auth.login(request, user)
            return redirect("/")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


