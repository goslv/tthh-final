from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class PerfilFuncionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cedula = models.CharField(max_length=45, unique=True)
    cargo = models.CharField(max_length=80)
    fecha_ingreso = models.DateField()
    departamento = models.CharField(max_length=100)
    estado = models.CharField(max_length=45)
    estado_civil = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    description = models.TextField()
    obligatorio = models.BooleanField()

    def __str__(self):
        return self.nombre

class DocumentoFuncionario(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(PerfilFuncionario, on_delete=models.CASCADE)
    id_tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    fecha_presentacion = models.DateField()
    archivo = models.FileField(
        upload_to='documentos/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'doc', 'docx'])],
        null=True,
        blank=True
    )
    estado = models.CharField(max_length=45)

class EventoLaboral(models.Model):
    id_evento = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(PerfilFuncionario, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=100)
    motivo = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    url_resolucion_evento = models.FileField(
        upload_to='resoluciones/',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'])],
        blank=True,
        null=True 
    )
    

class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(PerfilFuncionario, on_delete=models.CASCADE)
    tipo_evaluacion = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)
    fecha = models.DateField()

class BeneficioFuncionario(models.Model):
    id_beneficio = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(PerfilFuncionario, on_delete=models.CASCADE)
    tipo_beneficio = models.CharField(max_length=100)
    description = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    url_resolucion_beneficios = models.FileField(
        upload_to='beneficios/',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'])],
        blank=True,
        null=True
    )
    
class PerfilUsuario(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=45)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.user.get_full_name()