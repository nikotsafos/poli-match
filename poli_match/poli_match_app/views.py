from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import *

from .models import Politician, Quote

def index(request):
    quotes = Quote.objects.all()
    return render(request, 'poli_match/index.html', {'quotes': quotes})

def quote_detail(request, pk):
    quote = Quote.objects.get(id=pk)
    return render(request, 'poli_match/quote_detail.html', {'quotes': quotes})

def politicians(request):
    politicians = Politician.objects.all()
    return render(request, 'poli_match/politicians.html', {'politicians': politicians})

def politician_detail(request, pk):
    politician = Politician.objects.get(id=pk)
    return render(request, 'poli_match/politician_detail.html', {'politicians': politicians})

# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request, 'poli_match/signup.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        try:
            user = User.objects.create_user(username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name)
            if user is not None:
                return login(request)
        except:
            return render(request, 'poli_match/signup.html', { 'error': 'arrg' })

def login(request):
    if request.method == 'GET':
        return render(request, 'poli_match/login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'poli_match/index.html')
        else:
            return render(request, 'poli_match/login.html', { 'error': 'invalid credentials' })

def logout(request):
    auth.logout(request)
    return render(request, 'poli_match/index.html')