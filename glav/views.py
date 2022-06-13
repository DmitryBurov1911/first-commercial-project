from unicodedata import name
from django.shortcuts import render

def index(request):
    data = {
        'title' : 'Главная',
    }

    return render(request, "glav/index.html", data)

def about(request):
    return render(request, "glav/about.html")

def news_home(request):
    return render(request, "news/news_home")