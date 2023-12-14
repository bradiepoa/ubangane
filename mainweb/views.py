from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta


def home(request):
    current_time = datetime.now()
    expiration_time = current_time + timedelta(days=30)

    if current_time < expiration_time:
        # Display the normal content
        return render(request, "mainweb/index.html")
    else:
        return HttpResponse("Please contact the developer @Bradie poa")


def About(request):
    
    return render(request,"mainweb/aboutus.html")


def Products(request):
    
    return render(request,"mainweb/products.html")


def Blog(request):
    
    return render(request,"mainweb/news.html")


def Contact(request):
    
    return render(request,"mainweb/contactus.html")

