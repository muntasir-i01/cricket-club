from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def members(request):
    return HttpResponse("Hello python django!")
