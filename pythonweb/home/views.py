from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from .forms import RegistrationForm

def index(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def error(request, exception):
    return render(request, 'error.html', status=404)

def register(request):
    form = RegistrationForm()  # Define the form here

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  
    
    return render(request, 'pages/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('index')  # Chuyển hướng về trang chủ

