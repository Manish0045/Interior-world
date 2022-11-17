from asyncio.windows_events import NULL
from enum import auto
import profile
from pyclbr import Class
from tkinter import CASCADE
from django.db import models

from Interior_app.views import contact

# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    subject=models.CharField(max_length=15)
    message=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class register(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=30)
    unm=models.CharField(max_length=10)
    pwd=models.CharField(max_length=8)
    pwd1=models.CharField(max_length=8)
    
    def __str__(self):
        return self.unm
    
class appointment(models.Model):
    Uname=models.CharField(max_length=50)
    Uphone=models.CharField(max_length=10)
    Uemail=models.EmailField(max_length=20)
    Uaddress=models.CharField(max_length=30)
    Udate=models.DateField()
    Utime=models.TextField(max_length=8)
    Umessage=models.CharField(max_length=8)
    
    def __str__(self):
        return self.name
    
class Contractors(models.Model):
    C_id=models.AutoField(primary_key=True)
    Profile_pic=models.ImageField()
    Contractor_name=models.CharField(max_length=10)
    contact=models.IntegerField()
    projects=models.ImageField()
    address=models.CharField(max_length=30)
    def __str__(self):
        return self.Contractor_name

class Interiors(models.Model):
    I_id=models.IntegerField(default=100)
    C_id=models.ForeignKey('Contractors',on_delete=models.CASCADE)
    Interior_name=models.CharField(max_length=15)
    contact=models.IntegerField()
    address=models.CharField(max_length=35)
    projects=models.ImageField()
    
    def __str__(self):
        return self.Interior_name
    