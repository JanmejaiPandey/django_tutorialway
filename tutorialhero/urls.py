from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    # path('home/',views.home,name="home"),
    path('python3/',views.python3,name='python3'),
    path('html/',views.html,name="html"),
    path('about/',views.about,name="about"),
    path('c/',views.c,name="c"),
    path('numpy/',views.numpy,name="numpy"),
    path('pandas/',views.pandas,name="pandas"),
    path('css/',views.css,name="css"),
    path('search/',views.SearchView,name="query"),
    path('admin/', admin.site.urls),
    path('home/',views.ProductListView.as_view(),name="home"),
    path('',views.start_page,name="start"),
]
urlpatterns += [
      path('python3-first-step/',views.pyfirst,name="pyfirst"),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('signup/',views.SignUp_page,name="signup"),
]
#for dictionary
urlpatterns += [
   path('dictionary/',views.dictionary,name="dictionary"),
   path('dictionary/variable/',views.variable,name="variable")
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)