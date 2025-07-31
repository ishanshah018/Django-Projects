from django.db import models

# Create your models here.

class Book(models.Model):
    b_name=models.CharField(max_length=100)
    a_name=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.b_name}-{self.a_name}"