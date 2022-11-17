from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('',views.home),
    path('pagenotfound',views.pagenotfound, name="pagenotfound"),
    path('FAQ',views.FAQ, name="FAQ"),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    path('feedback',views.feedback, name="feedback"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('services',views.services, name="services"),
    path('appointment',views.appointment, name="appointment")
]
