from django.shortcuts import render
from django.http import request

def python3(request):
    return render(
        request,
        'python3.html',
    )

def home(request):
    return render(
        request,
        'home.html',
    )

def html(request):
    return render(
        request,
        'html.html',
    )

def about(request):
    return render(
        request,
        'about.html',
    )
