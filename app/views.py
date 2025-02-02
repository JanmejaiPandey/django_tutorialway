from django.shortcuts import render,redirect
from django.http import request
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,get_user_model,logout 
from django.urls import reverse_lazy
from django.views import generic
from tutorialhero import urls
from .forms import LoginForm,SignUpForm
import urllib
from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
from django.http import request
from .models import product

class ProductFeaturedListView(ListView):
    template_name = "home.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return product.objects.all().featured ()


class ProductListView(ListView):
    queryset = product.objects.all()
    template_name = "home.html"
    
    # def get_context_data(self, *args, **kwargs ):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return product.objects.all()

def product_list_view(request):
    queryset = product.objects.all()
    context = {
        'object_list':queryset,
    }
    return render(
        request,
        "home.html",
        context
        )

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
def SearchView(request):
     return render( 
        request,
        'search/search.html',
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
def dictionary(request):
    return render(
        request,
        'dictionary/dictionary.html',
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
        "form" : form,
        "title": "Login",
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
            #context['form'] = LoginForm()
            return redirect("/")       
        else:
            print("Error")
    
    return render(
        request,
        "auth/login.html",
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
        if new_user is not None:
            return redirect("/login")       
    return render(
        request,
        "auth/signup.html",
        context
        )

def pyfirst(request):
    return render(
        request,
        'content/python3/first.html',
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

