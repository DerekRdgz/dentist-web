from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def rakurai(request):
    return render(request, 'rakurai.html',{})

# Create your views here.
