from django.shortcuts import render, redirect
from django.http import HttpResponse # agregamos el HttpResponse
from .models import FUT
from datetime import date

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

        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')

        response = redirect('lol')

        response.set_cookie('c_name', name)
        response.set_cookie('c_program', program)
        response.set_cookie('c_dni', dni)
        response.set_cookie('c_phone', phone)
        response.set_cookie('c_cycle', cycle)

        return response


def create_fut_process(request):
    if request.method=='GET':
        print('MMMMMMMMMMM')
        #name = request.COOKIES['c_name'] #obtenemos el cookie
        #print(name)
        print('MMMMMMMMMMM')
        return render(request, 'create_fut/process.html')
    if request.method=='POST':
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        reason = request.POST.get('reason')

        response = redirect('pay')

        response.set_cookie('c_myrequest', myrequest)
        response.set_cookie('c_order', order)
        response.set_cookie('c_reason', reason)

        return response
    
def create_fut_pay(request):
    if request.method=='GET':
        return render(request, 'create_fut/pay.html')
    if request.method=='POST':
        v_name = request.COOKIES['c_name'] #obtenemos el cookie
        v_program = request.COOKIES['c_program']
        v_dni = request.COOKIES['c_dni']
        v_phone = request.COOKIES['c_phone']
        v_cycle = request.COOKIES['c_cycle']
        v_myrequest = request.COOKIES['c_myrequest']
        v_order = request.COOKIES['c_order']
        v_reason = request.COOKIES['c_reason']
        

        v_now_date = date.today()

        my_objet = FUT(name=v_name, program=v_program, dni=v_dni, phone=v_phone, cycle=v_cycle, myrequest=v_myrequest, order=v_order, reason=v_reason, date=v_now_date)

        my_objet.save()
    
        print(v_name+' - '+v_program+' - '+v_dni+' - '+v_phone+' - '+v_cycle+' - '+v_myrequest+' - '+v_order+' - '+v_reason)

        return render(request, 'create_fut/pay.html')