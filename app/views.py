from django.shortcuts import render
from django.http import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

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
@login_required
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

def login(request):
    return render(
        request,
        'login.html',
    )

def logout(request):
    return render(
        request,
        'logout.html',
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

