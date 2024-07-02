from django.shortcuts import render
from django.http import *


def home(request):
    return render(request, "index.html")
   
def success(request):
    print("okay")
    return HttpResponse("<h1> okay  </h1>")

def about(request):
    context={'page':'About'}
    return render (request,"about.html",context)