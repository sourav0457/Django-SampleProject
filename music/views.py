from django.shortcuts import render
from django.http import HttpResponse            #http response sends back html/basic webpage
from django.conf.urls import include

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is music app homepage</h1>")