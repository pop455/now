from django.contrib import admin, messages, auth
from django.shortcuts import render, redirect
from django.urls import path, include
from django.contrib.auth import views as auth_views

from restaurant.forms import UserRegistrationForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
    return  render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Register Successfully')
            form.save()
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


