from multiprocessing import context
from django.shortcuts import render

def mostrar_other(request):
    return render(request, 'manejador_contenido/other.html', {})

def mostrar_profile(request):
    return render(request, 'manejador_contenido/profile.html', {})
# Create your views here.
