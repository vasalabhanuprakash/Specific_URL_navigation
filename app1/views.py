from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Hardik(request):

    return HttpResponse('<center><h1>No.1 AllRounder in the world=Hardik Pandya')


def Virat(request):

    return HttpResponse('The Aggressive batsman of the World')