from django.urls import path
from . import views # corto y pego de ./mysite/urls.py

urlpatterns = [
    path('', views.index), # corto y pego de ./mysite/urls.py
    path('form_new_fut/identification', views.form_new_fut), #corto y pego de ./mysite/urls.py
    path('my_fut', views.my_fut),
    path('form_new_fut/processtd', views.create_fut_details, name="lol"),
    path('form_new_fut/pay', views.create_fut_pay)
]