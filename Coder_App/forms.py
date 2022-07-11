from django import forms

class CursoFormulario(forms.Form):
    #se especifican los campos
    nombre_curso = forms.CharField(required=False)
    camada = forms.IntegerField()
    
