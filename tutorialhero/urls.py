"""tutorialhero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('python3/',views.python3,name='python3'),
    path('html/',views.html,name="html"),
    path('about/',views.about,name="about"),
    path('c/',views.c,name="c"),
    path('numpy/',views.numpy,name="numpy"),
    path('pandas/',views.pandas,name="pandas"),
    path('css/',views.css,name="css"),
    path('search/',views.SearchView,name="query"),
    path('admin/', admin.site.urls),
    path('',views.start_page,name="start"),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('signup/',views.SignUp_page,name="signup"),
]
