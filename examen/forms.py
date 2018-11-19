from django import forms
from .models import Estudiante, Materia , Profesor, Grado

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'carne', 'materias')

    def __init__ (self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Ingrese los cursos a asignar al estudiante"
        self.fields["materias"].queryset = Materia.objects.all()

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre', 'descripcion', 'materias')

    def __init__ (self, *args, **kwargs):
        super(GradoForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Ingrese los cursos a asignar al estudiante"
        self.fields["materias"].queryset = Materia.objects.all()

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields =('nombre','descripcion','profesor',)
        widgets = {
            'profesor':forms.Select,
}

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido','edad',)
