from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'var':'This is WorldCount from python code'})

def Gym(request):
    return HttpResponse('<h1>Lets Go To The Gym!!')