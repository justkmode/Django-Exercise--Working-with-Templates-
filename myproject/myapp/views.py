from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Menu(request):
    return render(request, 'menu.html')

def Book(request):
    return render(request, 'book.html')
