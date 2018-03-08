from django.shortcuts import render
from django.http import HttpResponse
from .forms import RainForm
from .models import RainData
from decimal import Decimal


def home(request):
    if request.method == 'POST':
        form = RainForm(request.POST)

        if form.is_valid():
            
            roofArea = form.cleaned_data['roofArea']
            if form.cleaned_data['roofType'] == 'Tin':
                roofCoeff = Decimal('0.8')
            else:
                roofCoeff = Decimal('0.85')

            rainData = RainData.objects.get(latitude="51.47")
            finalRainData = rainData.rainWaterCalculation(roofArea, roofCoeff)
            


            return render(request, 'main/results.html', {'roofArea': roofArea, 'rainData' : finalRainData})
    else:
        form = RainForm()
    return render(request, 'main/home.html', {'rainform': RainForm()})

def assumptions(request):
    return render(request, 'main/assumptions.html')

def hardwarecomparison(request):
    return render(request, 'main/hardwarecomparison.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def spanish(request):
    return render(request, 'main/spanish.html')

def chinese(request):
    return render(request, 'main/chinese.html')

def rain_data(request):
    return render(request, 'main/rain_data.html')


