from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'library/index.html', {})

def authorization(request):
    return render(request, 'library/authorization.html', {})

def registration(request):
    return render(request, 'library/registration.html', {})