from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("request : ", request)
    print(dir(request))
    print(dir(request.user))
    return HttpResponse("<h1>Hello</h1>")
