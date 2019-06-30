from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def Gym(request):
    return HttpResponse('<h1>Lets Go To The Gym!!</h1>')

def count(request):
    fulltext=request.GET['fulltext']
    words=fulltext.split()
    l=len(words)
    return render(request,'count.html',{'len':l,'text':fulltext})