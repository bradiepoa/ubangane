from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    
    return render(request,"mainweb/index.html")

def Contact(request):
    
    return render(request,"mainweb/contactus.html")

