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
def signin(request):
    return render(
        request,
        'signin.html',
    )

def signup(request):
    return render(
        request,
        'signup.html',
    )


def c(request):
    return render(
        request,
        'c.html',
    )

def css(request):
    return render(
        request,
        'CSS.html',
    )

def numpy(request):
    return render(
        request,
        'numpy.html',
    )
def pandas(request):
    return render(
        request,
        'pandas.html',
    )

