from django.urls import path
from . import views # corto y pego de ./mysite/urls.py

urlpatterns = [
    path('', views.index), # corto y pego de ./mysite/urls.py
    path('form_new_fut/', views.form_new_fut) #corto y pego de ./mysite/urls.py
]