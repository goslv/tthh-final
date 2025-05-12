from django.contrib import admin
from .models import PerfilFuncionario, TipoDocumento, DocumentoFuncionario, Evaluacion, BeneficioFuncionario, EventoLaboral, PerfilUsuario


admin.site.register(PerfilUsuario)
admin.site.register(PerfilFuncionario)
admin.site.register(TipoDocumento)
admin.site.register(DocumentoFuncionario)
admin.site.register(Evaluacion)
admin.site.register(BeneficioFuncionario)
admin.site.register(EventoLaboral)

