from django.db import models

# Create your models here.
from django.contrib import admin
# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.nombre, self.apellido)

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

class Grado(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.IntegerField()
    materias   = models.ManyToManyField(Materia, through='Seccion')
    def __str__(self):
        return self.nombre

class Seccion (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    nota = models.CharField(max_length=60)

class SeccionInLine(admin.TabularInline):
    model = Seccion
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (SeccionInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (SeccionInLine,)
