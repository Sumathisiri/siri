from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def abc(request):
    return HttpResponse('<h1>abccccc....</h1>')

def virat(request):
    return HttpResponse('<h1>virat....</h1>')
