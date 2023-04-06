from django.shortcuts import render, redirect
from django.http import HttpResponse # agregamos el HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def my_fut(request):
    return render(request, 'view_fut/fut.html')

# Create FUT

    

def form_new_fut(request):
    if request.method=='GET':
        return render(request, 'create_fut/identification.html')
    if request.method=='POST':


        mycicle = request.POST.get('cicle')

        response = redirect('lol')

        response.set_cookie('ciclon', mycicle)
        return response


def create_fut_details(request):
    if request.method=='GET':
        print('MMMMMMMMMMM')
        name = request.COOKIES['ciclon'] #obtenemos el cookie
        print(name)
        print('MMMMMMMMMMM')
        return render(request, 'create_fut/process.html')
    if request.method=='POST':
        mycicle = request.POST.get('cicle')
        print('MMMMMMMMMMM')
        print('------'+mycicle)
        print(request.pepo)
        print('MMMMMMMMMMM')
        context = {
        }

        response = render(request, 'create_fut/process.html', context)
        # setting the cookies
        response.set_cookie('ciclon', mycicle)

        #response.redirect('lol')

        return response