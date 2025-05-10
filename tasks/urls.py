from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.menu_inicio, name='menu_inicio'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/crear/', views.crear_funcionario, name='crear_funcionario'),
    path('funcionarios/editar/<int:id_funcionario>/', views.actualizar_funcionario, name='actualizar_funcionario'),
    path('funcionarios/eliminar/<int:id_funcionario>/', views.eliminar_funcionario, name='eliminar_funcionario'),

    path('tipos-documento/', views.lista_tipos_documento, name='lista_tipos_documento'),
    path('tipos-documento/crear/', views.crear_tipo_documento, name='crear_tipo_documento'),

    path('documentos-funcionario/', views.lista_documentos, name='lista_documentos_funcionario'),
    path('documentos-funcionario/crear/', views.crear_documento, name='crear_documento'),
]
