from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Emobilis')

def programs(request):
    return HttpResponse('Front end, Back end, Fullstack')

def about(request):
    return HttpResponse('We dedicated to empower youths with the latest technology')