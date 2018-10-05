from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint

from .models import Politician, Quote

def index(request):
    quotes = Quote.objects.all()
    rand = randint(3,4,5,6,7,8,9,10,11,12,13)
    print('this is random quote', str(rand))
    return render(request, 'poli_match/index.html', {'quotes': quotes, 'rand': str(rand)})

def quote_detail(request, pk):
    quote = Quote.objects.get(id=pk)
    return render(request, 'poli_match/quote_detail.html', {'quote': quote})

def quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'poli_match/quotes.html', {'quotes': quotes})

def politicians(request):
    politicians = Politician.objects.all()
    return render(request, 'poli_match/politicians.html', {'politicians': politicians})

def politician_detail(request, pk):
    politician = Politician.objects.get(id=pk)
    rand = randint(3,4,5,6,7,8,9,10,11,12,13)
    return render(request, 'poli_match/politician_detail.html', {'politician': politician, 'rand': rand})

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
        print("HITTING THE THING WE WANT TO HIT")
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'poli_match/login.html', { 'error': 'invalid credentials' })

def logout(request):
    auth.logout(request)
    return redirect('index')