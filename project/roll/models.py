from django.db import models

# Create your models here.

class Student(models.Model):
    stuid=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    result=models.CharField()    