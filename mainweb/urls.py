from django.urls import path
from .import views

app_name = 'mainweb'
urlpatterns = [

    path("", views.home, name="home"),
    path("abouts-us", views.About, name="abouts-us"),
    path("products", views.Products, name="products"),
    path("updates", views.Blog, name="updates"),
    path("contactus", views.Contact, name="contactus"),
   
    
]