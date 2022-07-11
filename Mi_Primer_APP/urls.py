"""Mi_Primer_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Coder_App.views import (prueba, mostrar_index, listar_familiar, listar_cursos)
from manejador_contenido.views import (mostrar_other, mostrar_profile)

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'saludar/', prueba),
    path( 'index/', mostrar_index),
    path( 'familiares/', listar_familiar),
    path( 'cursos/', listar_cursos),
    path( 'other/', mostrar_other),
    path( 'profile/', mostrar_profile),
]
