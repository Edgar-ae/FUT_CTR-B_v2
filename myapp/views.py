from asgiref.sync import sync_to_async, async_to_sync
import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse # agregamos el HttpResponse
from .models import fut
from datetime import date
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

#pip install qrcode
import random, qrcode

#pip install opencv-python-headless
import cv2
import base64

import string

from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def my_fut(request):

    return render(request, 'view_fut/fut.html')



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

# para generear el expediente
async def generate_proceedings():
    # Genramos el número de Expediente
    Expediente = random.sample(range(0, 9),5)
    exp_ = ''.join(map(str, Expediente))
    # Generamos la contraseña
    Contraseña = random.sample(range(0, 9),4)
    pas_ = ''.join(map(str, Contraseña))

    return exp_, pas_


async def generate_code():
    caracteres = string.ascii_letters + string.digits
    code = ''.join(random.choice(caracteres) for i in range(11))
    return code

@sync_to_async
def save_my_objet(name, program, dni, phone, cycle, myrequest, order, reason, now_date, pdf_bytes, exp_, pas_, code_, qrimg_bytes):
    my_objet = fut(name=name, program=program, dni=dni, phone=phone, cycle=cycle, myrequest=myrequest, order=order, reason=reason, date=now_date, pdf_binary=pdf_bytes, proceeding=exp_, password=pas_, code=code_, qrimg_binary=qrimg_bytes)
    my_objet.save()
    new_id = my_objet.id
    return new_id

async def generate_qrcode(code_):
    print('Hay que crear el QR!')

    input = 'http://127.0.0.1:8000/my_fut/proceedings?code='+code_

    qr = qrcode.QRCode(version=1, box_size=10, border=3)

    qr.add_data(input)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    static_path = 'myapp/static/tmp/'+code_+'qrcode.png'

    print(static_path)
    img.save(static_path)
    img = cv2.imread('qrtelecapp.png')
    
    # Codificar la imagen en formato PNG
    retval, buffer = cv2.imencode('.png', img)

    # Convertir el buffer a bytes
    img_bytes = buffer.tobytes()

    # Codificar los bytes en base64
    img_base64 = base64.b64encode(img_bytes)

    # print(img_base64)

    return img_base64


async def finisher(request):
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
        
        exp_, pas_ = await generate_proceedings()
        code_ = await generate_code()
        qrimg_bytes = await generate_qrcode(code_)

        new_id = await save_my_objet(name, program, dni, phone, cycle, myrequest, order, reason, now_date, pdf_bytes, exp_, pas_, code_, qrimg_bytes)

        response = redirect('n_successful')
        response.set_cookie('New_id', new_id)
        return response
    
    else:
        return HttpResponse("<h1>404 Not Found :(</h1>")
    
    
def successful(request):
    my_id = request.COOKIES.get('New_id')
    objetos = fut.objects.filter(id=my_id).values('name', 'dni', 'order', 'proceeding', 'password', 'code').first()
    return render(request, 'create_fut/successful.html', {
        'Name': objetos['name'],
        'Dni': objetos['dni'],
        'Order': objetos['order'],
        'Code': objetos['code'],
        'Proceeding': objetos['proceeding'],
        'Password': objetos['password']
    })

def proceedings(request):
    code_ = request.GET.get('code')
    object = fut.objects.filter(code=code_).values('name', 'dni', 'order', 'proceeding', 'password', 'code', 'program').first()
    dni = str(object['dni'][:3])
    # My params for css
    progressbar = [1,2,3,4,5,6] # for progress bar lines
    details = [1,2,3]# for details picture
    left = 20 # css left details picture
    return render(request, 'view_fut/proceedings.html', {
        'Name': object['name'],
        'Dni': dni,
        'Order': object['order'],
        'Proceeding': object['proceeding'],
        'Program': object['program'],
        'Progressbar': progressbar,
        'Details': details,
        'Left': left
    })


