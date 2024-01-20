from django.db import models
from django.contrib.auth.models import User
class Watches(models.Model):
    brand=models.CharField(max_length=250)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    price=models.IntegerField(max_length=200)
    image1=models.ImageField(upload_to='gallery')
    image2=models.ImageField(upload_to='gallery')
    image3=models.ImageField(upload_to='gallery')
    color=models.CharField(max_length=200)
    material=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
# Create your models here.
