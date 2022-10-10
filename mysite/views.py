import imp
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import News
# Create your views here.

def index(request):
    return render(request,'home.html',locals())

def lotto(request):
    lucky=[]
    for i in range(0,6):lucky.append(random.randint(1,99))
    return render(request,'lotto.html',locals())

def showall(request):
    news=News.objects.all()
    return render(request,'showall.html',locals())

def show(request):
    target = News.objects.get(title="Hello")
    return render(request,'show.html',locals())