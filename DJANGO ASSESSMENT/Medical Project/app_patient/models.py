from django.db import models

# Create your models here.
from app_patient.models import *
from app_doctor.models import *
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    propic=models.FileField(upload_to="media/",default="anonymous.png")

    def __str__(self):
        return str(self.name)
    
class Appointment(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    date = models.DateField(auto_now_add=True)
    department=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    messege=models.CharField(max_length=500)

