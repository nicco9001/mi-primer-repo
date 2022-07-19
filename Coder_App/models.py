from django.db import models

class Familia(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.camada}"
# Create your models here.
