from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def IMC(request):
    return HttpResponse(str(75/(1.8**2)))
