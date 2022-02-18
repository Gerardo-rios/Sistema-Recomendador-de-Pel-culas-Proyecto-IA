from django.template import RequestContext
from django.shortcuts import render

def homePage(request):
    return render(request,'home_Page.html')

def listMovies(request):
    return render(request, 'movielist.html')