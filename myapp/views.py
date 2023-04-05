from django.shortcuts import render
from django.http import HttpResponse # agregamos el HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def my_fut(request):
    return render(request, 'view_fut/fut.html')

# Create FUT

def form_new_fut(request):
    return render(request, 'create_fut/identification.html')

def create_fut_details(request):
    return render(request, 'create_fut/process.html')