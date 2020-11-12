from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from Book.models import User


def main_page(request):
    return render(request, 'Main.html')

def sign_up(request):
    return render(request, 'Sign_up.html')

def log_in(request):
    return render(request, 'Log_in.html')

def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password']
    )
    login(request, user)
    return HttpResponseRedirect('/start')

# Create your views here.
