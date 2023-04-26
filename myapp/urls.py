from django.urls import path
from . import views # corto y pego de ./mysite/urls.py

urlpatterns = [
    path('', views.index), # corto y pego de ./mysite/urls.py
    path('form_new_fut/identification', views.form_new_fut), #corto y pego de ./mysite/urls.py
    path('my_fut', views.my_fut),
    path('form_new_fut/processtd', views.create_fut_process, name="n_process"),
    path('form_new_fut/pay', views.create_fut_pay, name="n_pay"),
    path('form_new_fut/finisher', views.finisher, name="n_end"),
    path('form_new_fut/successful', views.successful, name="n_successful"),

    path('my_fut/subir_pdf', views.subir_pdf, name="subir_pdf")
]