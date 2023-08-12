from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Blog(models.Model):
    titel=models.CharField(max_length=50)
    # name=models.CharField(max_length=50)
    content=models.CharField(max_length=500)
    created_at=models.DateTimeField(max_length=50)
    Update=models.DateTimeField(max_length=100)


    def __str__(self):
      return self.titel