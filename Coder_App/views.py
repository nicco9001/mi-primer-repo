from datetime import datetime
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from Coder_App.models import (Familia, Curso)
from Coder_App.forms import CursoFormulario

def prueba(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse (f"Esto es una prueba, la fecha de hoy es {fecha_hora_ahora}")

def mostrar_index(request):
    return render(request, "Coder_App/index.html", {"mi_titulo":"Mi Primer Website"})

def listar_familiar(request):
    context = {}
    context["familiares"] = Familia.objects.all()
    return render (request, 'Coder_App/Familia.html', context)

def listar_cursos(request):
    context = {}
    context["cursos"] = Curso.objects.all() #KEY que se usa luego en el HTML.-
    return render (request, 'Coder_App/Curso.html', context)

def formulario_curso(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST) #acá llega la información de la HTML.-

        if  mi_formulario.is_valid():     #Si pasa la validación de Django
            datos = mi_formulario.cleaned_data 
            # acá se instancia el curso:
            curso = Curso(nombre = datos["nombre_curso"], modalidad = datos["modalidad"], camada = datos["camada"])
            #Curso refiere al modelo, los keys al forms.-
            curso.save()
        return render(request, "Coder_App/index.html")
   
    else:
        mi_formulario = CursoFormulario()
        return render(request, "Coder_App/curso_formulario.html", {"mi_formulario":mi_formulario})

# Create your views here.
