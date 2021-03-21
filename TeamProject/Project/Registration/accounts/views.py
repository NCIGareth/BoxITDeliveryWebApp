from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render( request, 'index.html');

def become(request):
    return render( request, 'Become-a-driver.html');

def login(request):
    if request.method == 'POST':
        password = request.POST['password'] 
        username = request.POST['username']

        user = auth.authenticate(username=username, password=password)

        if user is not None: 
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'sign-in.html')


def register(request):

    if request.method == 'POST':
        first_name=request.POST.get("first_name", "default value")
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'Sign-up.html')