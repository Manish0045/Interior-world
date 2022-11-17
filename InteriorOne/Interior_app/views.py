from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def pagenotfound(request):
    return render(request,'404.html')

def FAQ(request):
    return render(request,'FAQ.html')

def login(request):
    return render(request,'forms/login.html')

def register(request):
    if request.method=="POST":
        register=register()
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        unm=request.POST.get('unm')
        pwd=request.POST.get('pwd')
        pwd1=request.POST.get('pwd1')
        
        register.fname=fname
        register.lname=lname
        register.unm=unm
        register.pwd=pwd
        register.pwd1=pwd1
        
        register.save()
        return render(request,'forms/login.html')
    
    return render(request,'forms/register.html')

def feedback(request):
    if request.method=="POST":
        feedback=feedback()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        feedback.name=name
        feedback.email=email
        feedback.subject=subject
        feedback.message=message
        
        feedback.save()
        return render(request,'index.html')
        
    return render(request,'forms/feedback.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def appointment(request):
    if request.method=="POST":
        appointment=appointment()
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        date=request.POST.get('date')
        time=request.POST.get('time')
        message=request.POST.get('message')
        
        appointment.name=name
        appointment.phone=phone
        appointment.email=email
        appointment.address=address
        appointment.date=date
        appointment.time=time
        appointment.message=message
        
        appointment.save()
        return render(request,'index.html')
        
    return render(request,'Appointment.html')