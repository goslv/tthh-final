from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_inicio, name='menu_inicio'),  # <--- ESTA debe ser la primera
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/crear/', views.crear_funcionario, name='crear_funcionario'),
    path('funcionarios/editar/<int:id_funcionario>/', views.actualizar_funcionario, name='actualizar_funcionario'),
    path('funcionarios/eliminar/<int:id_funcionario>/', views.eliminar_funcionario, name='eliminar_funcionario'),

    path('tipos-documento/', views.lista_tipos_documento, name='lista_tipos_documento'),
    path('tipos-documento/crear/', views.crear_tipo_documento, name='crear_tipo_documento'),

    path('documentos-funcionario/', views.lista_documentos, name='lista_documentos_funcionario'),
    path('documentos-funcionario/crear/', views.crear_documento, name='crear_documento'),
]
