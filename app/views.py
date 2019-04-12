from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,get_user_model,logout 
from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginForm,SignUpForm

User =get_user_model()
def python3(request):
    context = {
        "title":"PYTHON TUTORIAL"
    }
    return render(
        request,
        'python3.html',
        context
    )

def home(request):
    return render(
        request,
        'home.html',
    )
# @login_required
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

def start_page(request):
    context = {
        "title":"TutorialHero"
    }
    return render(
        request,
        'start.html',
    )

def login_page(request):
    form = LoginForm(request.POST or None)
    print("User LoggedIn is")
    print(request.user.is_authenticated)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #print(request.user.is_authenticated)
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print(request.user.is_authenticated)
            #context['form'] = LoginForm()
            return redirect("/")       
        else:
            print("Error")

    return render(
        request,
        'auth/login.html',
        context
    )

def logout_page(request):
    
    return render(
        logout(request),
        'auth/logout.html',
    )

def SignUp_page(request): 
    form = SignUpForm(request.POST or None)
    context={
        "form" : form,
        "title": "SignUp",
    }   
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)   
    return render(
        request,
        "auth/signup.html",
        context
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

