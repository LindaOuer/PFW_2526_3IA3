from django.db import models

# Create your models here.
class Classe(models.Model):
    className = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    year = models.IntegerField() 

class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    date_Of_Birth = models.DateField()
    cl = models.ForeignKey(Classe, on_delete=models.CASCADE)