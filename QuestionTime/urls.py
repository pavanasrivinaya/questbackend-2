"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [

    #admin urls
    path('admin/', admin.site.urls),

    #custom version of the registration view provided by django registration that it is 
    #used to create new accounts via browser
    path("accounts/register/",

         RegistrationView.as_view(

             form_class=CustomUserForm,

             success_url="/",

             ), name="django_registration_register"), 

    #it is used by the dango registration package
    path("accounts/", 

         include("django_registration.backends.one_step.urls")),
    
    #login urls provided by django o login users via a broswer
    path("accounts/",include("django.contrib.auth.urls")),
    
    path("api/", include("users.api.urls")),

        path("api/", include("questions.api.urls")),

   
   #login url for the browserable API 
    path("api-auth/", include("rest_framework.urls")),

    #endpoints sto use the rest
    path("api/rest-auth/", include("rest_auth.urls")),
    
    #endpoint to use the registration
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
    ]
