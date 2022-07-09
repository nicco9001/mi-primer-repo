from django.db import models

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)
    camada = models.IntegerField()
# Create your models here.
