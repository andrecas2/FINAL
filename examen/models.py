from django.db import models
from django.contrib import admin

class Materia(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion  =   models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

class Estudiante(models.Model):
    nombre    = models.CharField(max_length=60)
    carne      = models.IntegerField()
    materias   = models.ManyToManyField(Materia, through='Asignacion')
    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class EstudianteAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
