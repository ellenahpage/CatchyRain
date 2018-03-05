from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')

def whyRWH(request):
    return HttpResponse("RWH Information")

def placeholder(request):
    return HttpResponse("placeholder")

def rain_data(request):
    return render(request, 'main/rain_data.html')


