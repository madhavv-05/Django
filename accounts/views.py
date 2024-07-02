from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trial(request):
    print("okay")
    return HttpResponse("<h1> it works  </h1>")
