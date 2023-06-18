from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello bro')

def brothers(request):
    return render(request,"home/index.html")
    


