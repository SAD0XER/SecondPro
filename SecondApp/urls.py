from django.contrib import admin
from django.urls import path
from django.urls import include
from SecondApp import views

urlpatterns = [
    path("", views.home, name='home'), #here you're adding visual pages and their names.
    path("home", views.home, name='home'),
    path("about", views.about, name='about'),
    path("signup", views.signUp, name='signup'),
    path("login", views.LogIn, name='login'),
    path("logout", views.LogOut, name='logout')
]