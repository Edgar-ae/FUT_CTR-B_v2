from django.db import models

# Create your models here.

class FUT(models.Model):
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    dni = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    cycle = models.CharField(max_length=2)

    myrequest = models.TextField()
    order = models.CharField(max_length=300)
    reason = models.TextField()

    date = models.DateField()

class PDF(models.Model):
    binary_content = models.BinaryField()

    