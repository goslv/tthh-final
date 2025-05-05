from django.contrib import admin
from .models import PerfilFuncionario, TipoDocumento, DocumentoFuncionario

admin.site.register(PerfilFuncionario)
admin.site.register(TipoDocumento)
admin.site.register(DocumentoFuncionario)

