from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    
    return render(request,"mainweb/index.html")

def About(request):
    
    return render(request,"mainweb/aboutus.html")


def Products(request):
    
    return render(request,"mainweb/products.html")


def Blog(request):
    
    return render(request,"mainweb/news.html")


def Contact(request):
    
    return render(request,"mainweb/contactus.html")

