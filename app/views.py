from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Dhoni(request):
    
    return HttpResponse('<h1>Dhoni is the No.1 Cricketer in the worl</h1>')
