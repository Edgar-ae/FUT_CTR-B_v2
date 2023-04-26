import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse # agregamos el HttpResponse
from .models import fut
from datetime import date
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

import random

# Create your views here.

def index(request):
    return render(request,'index.html')

def my_fut(request):

    print('Hay que crear el QR!')
    
    return render(request, 'view_fut/fut.html')
# Create FUT

    

def form_new_fut(request):
    return render(request, 'create_fut/identification.html')


def create_fut_process(request):
    if request.method=='POST':
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')

        return render(request, 'create_fut/process.html', {
            'Name': name,
            'Program': program,
            'Dni': dni,
            'Phone': phone,
            'Cycle': cycle
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")

    
@csrf_exempt  
def create_fut_pay(request):
    if request.method=='POST':
        # identification
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        # process
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        reason = request.POST.get('reason')
        # Procedimiento con el PDF
        pdf_file = request.FILES['pdf_file']
        pdf_binary = pdf_file.read()
        pdf_binary_encoded = base64.b64encode(pdf_binary)

        return render(request, 'create_fut/pay.html', {
            'Name': name,
            'Program': program,
            'Dni': dni,
            'Phone': phone,
            'Cycle': cycle,
            'Myrequest': myrequest,
            'Order': order,
            'Reason': reason,
            'Pdf_binary_encoded': pdf_binary_encoded
        })
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")

@csrf_exempt  
def finisher(request):
    if request.method == 'POST':
         # identification
        name = request.POST.get('name')
        program = request.POST.get('program')
        dni = request.POST.get('dni')
        phone = request.POST.get('phone')
        cycle = request.POST.get('cycle')
        # process
        myrequest = request.POST.get('myrequest')
        order = request.POST.get('order')
        reason = request.POST.get('reason')
        pdf_memoryview = request.POST.get('pdf_binary_encoded')
        pdf_bytes = pdf_memoryview.encode("utf-8")

        now_date = date.today()
        
        # Genramos el número de Expediente
        Expediente = random.sample(range(0, 9),5)
        Expediente_cadena = ''.join(map(str, Expediente))
        # Generamos la contraseña
        Contraseña = random.sample(range(0, 9),4)
        Contraseña_cadena = ''.join(map(str, Contraseña))

        my_objet = fut(name=name, program=program, dni=dni, phone=phone, cycle=cycle, myrequest=myrequest, order=order, reason=reason, date=now_date, binary_content=pdf_bytes, proceeding=Expediente_cadena, password=Contraseña_cadena)
        my_objet.save()

        new_id = my_objet.id

        response = redirect('n_successful')
        response.set_cookie('New_id', new_id)
        return response
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
    
    
def successful(request):
    my_id = request.COOKIES.get('New_id')
    objetos = fut.objects.filter(id=my_id).values('name', 'dni', 'order').first()
    return render(request, 'create_fut/successful.html', {
        'Name': objetos['name'],
        'Dni': objetos['dni'],
        'Order': objetos['order']
    })



@csrf_exempt
def subir_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']
        pdf_binary = pdf_file.read()
        pdf_binary_encoded = base64.b64encode(pdf_binary)
        pdf = PDF(binary_content=pdf_binary_encoded)
        pdf.save()
        print(',,,,,,,,,')
        return render(request, 'view_fut/exito.html')
    else:
        print('............')
        return render(request, 'view_fut/fut.html')
