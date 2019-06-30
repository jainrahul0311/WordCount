from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def Gym(request):
    return HttpResponse('<h1>Lets Go To The Gym!!')