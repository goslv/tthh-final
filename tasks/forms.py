from django import forms
from .models import PerfilFuncionario
from django import forms
from .models import TipoDocumento, DocumentoFuncionario

class PerfilFuncionarioForm(forms.ModelForm):
    class Meta:
        model = PerfilFuncionario
        fields = '__all__'

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