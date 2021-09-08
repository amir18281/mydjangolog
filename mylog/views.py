from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    # return HttpResponse('home page')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('about Page')
    return render(request, 'about.html')
