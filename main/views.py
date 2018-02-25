from django.shortcuts import render
from django.http import HttpResponse


def base(request):
    return render(request, 'main/base.html')

def whyRWH(request):
    return HttpResponse("RWH Information")