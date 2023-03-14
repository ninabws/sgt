from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def greet(request, pessoa):
    return render(request, 'greet.html', {'name': pessoa})

def tiadozap(request, sobrinha):
    h = datetime.datetime.now()
    dia = int(h.strftime('%H'))
    booleano = bool
    if dia > 17:
        booleano= False
    else:
        booleano = True
        
    return render(request, 'tiadozap.html', {'name': sobrinha, 'dia':True})

def greeting(request, nome):
    return HttpResponse("<h1 style='color:cornflowerblue'>Olá %s</h1>" %nome)