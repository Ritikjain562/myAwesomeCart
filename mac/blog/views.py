from django.shortcuts import render

#creat your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'blog/index.html')
