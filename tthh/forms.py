from django import forms
from .models import PerfilFuncionario, TipoDocumento, DocumentoFuncionario, EventoLaboral, Evaluacion, BeneficioFuncionario, PerfilUsuario
from django.contrib.auth.models import User
from django.utils.timezone import now

class PerfilFuncionarioForm(forms.ModelForm):
    class Meta:
        model = PerfilFuncionario
        fields = ['nombre', 'apellido', 'cedula', 'cargo', 'fecha_ingreso', 'departamento', 'estado', 'estado_civil']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
        }

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nombre', 'description', 'obligatorio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'obligatorio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DocumentoFuncionarioForm(forms.ModelForm):
    class Meta:
        model = DocumentoFuncionario
        fields = ['id_funcionario', 'id_tipo_documento', 'fecha_presentacion', 'archivo', 'estado']
        widgets = {
            'id_funcionario': forms.Select(attrs={'class': 'form-control'}),
            'id_tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'fecha_presentacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EventoLaboralForm(forms.ModelForm):
    class Meta:
        model = EventoLaboral
        fields = ['id_funcionario', 'tipo_evento', 'motivo', 'fecha_inicio', 'fecha_fin', 'url_resolucion_evento']
        widgets = {
            'id_funcionario': forms.Select(attrs={'class': 'form-control'}),
            'tipo_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'url_resolucion_evento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['id_funcionario', 'tipo_evaluacion', 'resultado', 'fecha']
        widgets = {
            'id_funcionario': forms.Select(attrs={'class': 'form-control'}),
            'tipo_evaluacion': forms.TextInput(attrs={'class': 'form-control'}),
            'resultado': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class BeneficioFuncionarioForm(forms.ModelForm):
    class Meta:
        model = BeneficioFuncionario
        fields = [
            'id_funcionario','tipo_beneficio','description','fecha_inicio','fecha_fin','url_resolucion_beneficios'  
        ]
        widgets = {
            'id_funcionario': forms.Select(attrs={'class': 'form-control'}),
            'tipo_beneficio': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'url_resolucion_beneficios': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False, initial=True, label='Remember Me', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    


class RegistroForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    direccion = forms.CharField(max_length=150, required=False)
    telefono = forms.CharField(max_length=15, required=False)
    fecha_registro = forms.DateField(required=False)

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        PerfilUsuario.objects.create(
            user=user,
            direccion=data['direccion'],
            telefono=data['telefono'],
            fecha_registro=data['fecha_registro'] or now().date()
        )
        return user