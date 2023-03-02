from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def greeting(request, nome):
    return HttpResponse("<h1 style='color:cornflowerblue'>Olá %s</h1>" %nome)