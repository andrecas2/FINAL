from django.contrib import admin
from examen.models import Materia, MateriaAdmin, Estudiante, EstudianteAdmin

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
