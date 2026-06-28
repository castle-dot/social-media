from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

from .models import Profile


def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()


            # create profile
            Profile.objects.create(
                user=user
            )


            # automatically login
            auth_login(request, user)


            # send to settings
            return redirect('settings')


    else:

        form = UserCreationForm()


    return render(
        request,
        'signup.html',
        {'form':form}
    )


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def settings(request):
    return render(request, 'setting.html')
