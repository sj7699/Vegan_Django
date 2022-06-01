from django.shortcuts import render
from django.http import HttpResponse
# Create your views heref.
def index(request):
    return HttpResponse("hi!")
