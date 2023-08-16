from django.db import models

# Create your models here.

class Perfume(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(max_length=50)
    Update=models.DateTimeField(max_length=100)


    def __str__(self):
        return self.name