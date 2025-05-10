from .models import PerfilFuncionario
from django import forms
from .models import TipoDocumento, DocumentoFuncionario

class PerfilFuncionarioForm(forms.ModelForm):
    class Meta:
        model = PerfilFuncionario
        fields = ['nombre', 'apellido', 'cedula', 'cargo', 'fecha_ingreso', 
                  'departamento', 'estado', 'estado_civil']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')]),
            'estado_civil': forms.Select(choices=[
                ('Soltero', 'Soltero'),
                ('Casado', 'Casado'),
                ('Divorciado', 'Divorciado'),
                ('Viudo', 'Viudo'),
                ('Unión libre', 'Unión libre')
            ]),
        }

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = '__all__'
        widgets = {
            'obligatorio': forms.CheckboxInput(),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class DocumentoFuncionarioForm(forms.ModelForm):
    class Meta:
        model = DocumentoFuncionario
        fields = '__all__'
        widgets = {
            'fecha_presentacion': forms.DateInput(attrs={'type': 'date'}),
        }