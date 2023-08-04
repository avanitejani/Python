
from django.db import models

# Create your models here.
from app_doctor.models import *

# Create your models here.
class Doc_user(models.Model):
    name=models.CharField(max_length=50)
    
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    propic=models.FileField(upload_to="media/",default="anonymous.png")
    


    def __str__(self):
        return str(self.name)
    

class Profile(models.Model):
    doc_name=models.CharField(max_length=50)
    # doc_email=models.EmailField(unique=True)
    departments=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    doc_image=models.FileField(upload_to="media/",default="anonymous.jpg")
    doc_desc=models.TextField(max_length=500)
    doc_id=models.ForeignKey(Doc_user,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.doc_name)
