from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

def prueba(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse (f"Esto es una prueba, la fecha de hoy es {fecha_hora_ahora}")

# Create your views here.
