from django.shortcuts import render
from django.http import HttpResponse # agregamos el HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def form_new_fut(request):
    return render(request, 'create_fut/form_new_fut.html')