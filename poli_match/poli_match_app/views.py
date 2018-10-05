from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'poli_match/index.html')

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
            user = User.objects.create_user(email=email,
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
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('poli_match/index.html')
        else:
            return render(request, 'poli_match/login.html', { 'error': 'invalid credentials' })

def logout(request):
    auth.logout(request)
    return redirect('poli_match/index.html')