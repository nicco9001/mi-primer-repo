from datetime import datetime
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from Coder_App.models import (Familia, Curso)

def prueba(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse (f"Esto es una prueba, la fecha de hoy es {fecha_hora_ahora}")

def listar_familiar(request):
    context = {}
    context["familiares"] = Familia.objects.all()
    return render (request, 'Coder_App/Familia.html', context)

def listar_cursos(request):
    context = {}
    context["cursos"] = Curso.objects.all()
    return render (request, 'Coder_App/Curso.html', context)

# Create your views here.
