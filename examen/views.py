from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import EstudianteForm, MateriaForm, ProfesorForm, GradoForm
from examen.models import Estudiante, Asignacion, Materia, Profesor, Grado, Seccion

def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'])
            for materia_id in request.POST.getlist('materias'):
                seccion = Seccion(materia_id=materia_id, grado_id = grado.id)
                seccion.save()
                messages.add_message(request, messages.SUCCESS, 'grado Guardada Exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'grado/new_grado.html', {'formulario': formulario})


def estudiante_nuevo(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            estudiante = Estudiante.objects.create(nombre=formulario.cleaned_data['nombre'], carne=formulario.cleaned_data['carne'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, estudiante_id = estudiante.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'estudiante Guardada Exitosamente')
    else:
        formulario = EstudianteForm()
    return render(request, 'grado/estudiante_nuevo.html', {'formulario': formulario})
