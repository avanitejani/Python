from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50) 
    email=models.EmailField()
    passowed=models.CharField(max_length=70)

    def __str__(self):
        return self.firstname+' '+self.lastname
 