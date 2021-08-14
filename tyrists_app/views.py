from django.shortcuts import render

from .models import Tyrs
from  django.http import HttpResponse
# Create your views here.
def index(request):
    tyrss = Tyrs.objects.all()
    context={"title":"Главная страница с",
             "tyrss":tyrss
    }
    return render(request,"tyrists_app/index.html",context)
def dabout(request):
    return render(request,"tyrists_app/about.html")
def contacts(request):
    return render(request,"contacts.html")
def faq(request):
    return render(request,"tyrists_app/faq.html")