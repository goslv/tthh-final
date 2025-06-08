from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view, logout_view, signup_view, test_template

urlpatterns = [
    

    # Test
    path('test/', test_template),

    #Autenticación
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.menu_inicio, name='menu_inicio'),

    # Funcionario
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/crear/', views.crear_funcionario, name='crear_funcionario'),
    path('funcionarios/editar/<int:id_funcionario>/', views.editar_funcionario, name='actualizar_funcionario'),
    path('funcionarios/eliminar/<int:id_funcionario>/', views.eliminar_funcionario, name='eliminar_funcionario'),

    # Documentos
    path('documentos/', views.lista_documentos, name='lista_documentos'),
    path('tipos-documento/', views.lista_tipos_documento, name='lista_tipos_documento'),
    path('tipos-documento/crear/', views.crear_tipo_documento, name='crear_tipo_documento'),
    path('documentos-funcionario/', views.lista_documentos, name='lista_documentos_funcionario'),
    path('documentos-funcionario/crear/', views.crear_documento, name='crear_documento'),
    path('documentos-funcionario/editar/<int:id_documento>/', views.editar_documento, name='editar_documento'),
<<<<<<< HEAD
=======
    path('tipos-documento/editar/<int:pk>/', views.editar_tipo_documento, name='editar_tipo_documento'),
    path('tipos-documento/eliminar/<int:pk>/', views.eliminar_tipo_documento, name='eliminar_tipo_documento'),
    path('documentos/', views.lista_documentos, name='lista_documentos'),
    path('documentos/crear/', views.crear_documento, name='crear_documento'),
    path('documentos/editar/<int:id_documento>/', views.editar_documento, name='editar_documento'),
    path('documentos/eliminar/<int:id_documento>/', views.eliminar_documento, name='eliminar_documento'),


>>>>>>> branch-RossNuevo

    # Evaluaciones
    path('evaluaciones/', views.lista_evaluaciones, name='lista_evaluaciones'),
    path('evaluaciones/crear/', views.crear_evaluacion, name='crear_evaluacion'),
    path('evaluaciones/editar/<int:id>/', views.editar_evaluacion, name='editar_evaluacion'),
    path('evaluaciones/eliminar/<int:id>/', views.eliminar_evaluacion, name='eliminar_evaluacion'),

    # Beneficios
    path('beneficios/', views.lista_beneficios, name='lista_beneficios'),
    path('beneficios/crear/', views.crear_beneficio, name='crear_beneficio'),
<<<<<<< HEAD
    path('beneficios/editar/<int:id>/', views.editar_beneficio, name='editar_beneficio'),
    path('beneficios/eliminar/<int:id>/', views.eliminar_beneficio, name='eliminar_beneficio'),

    # Eventos Laborales
    path('eventos/', views.lista_eventos_funcionario, name='lista_eventos'),
    path('eventos/crear/', views.registrar_evento_funcionario, name='crear_evento'),
    path('eventos/editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
=======
    path('beneficios/editar/<int:id_beneficio>/', views.editar_beneficio, name='editar_beneficio'),
    path('beneficios/eliminar/<int:id>/', views.eliminar_beneficio, name='eliminar_beneficio'),

    # Eventos Laborales
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/editar/<int:id_evento>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:id_evento>/', views.eliminar_evento, name='eliminar_evento'),

>>>>>>> branch-RossNuevo

    # Cambiar contraseña
    path('cambiar_contrasena/', auth_views.PasswordChangeView.as_view(template_name='tasks/cambiar_contrasena.html'), name='cambiar_contrasena'),
    path('cambiar_contrasena/done/', auth_views.PasswordChangeDoneView.as_view(template_name='tasks/cambiar_contrasena_done.html'), name='password_change_done'),
    # Restablecer contraseña
    path('restablecer_contrasena/', auth_views.PasswordResetView.as_view(template_name='tasks/restablecer_contrasena.html'), name='restablecer_contrasena'),
    path('restablecer_contrasena/done/', auth_views.PasswordResetDoneView.as_view(template_name='tasks/restablecer_contrasena_done.html'), name='password_reset_done'),
    path('restablecer_contrasena/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tasks/restablecer_contrasena_confirmar.html'), name='password_reset_confirm'),
    path('restablecer_contrasena/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='tasks/restablecer_contrasena_complete.html'), name='password_reset_complete'),
    
]
