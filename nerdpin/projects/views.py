from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("It works bishhh")