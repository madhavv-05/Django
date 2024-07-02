from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)
    address=models.TextField()
    file=models.FileField()

class product(models.Model):
    pass

class car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField()