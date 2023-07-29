from django.db import models

# Create your models here.
class User(models.Model):
    salutation=models.CharField(max_length=25)
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25) 
    gender=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    language=models.CharField(max_length=50)

    def __str__(self):
        return self.salutation+' '+self.lastname
 # 6--creating datatbase

# python manage.py makemigrations
# python manage.py migrate

# 7---running your project
# python manage.py runserver