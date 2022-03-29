from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    phone = models.CharField(max_length=13,unique=True)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=70,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


