from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PerfilUsuario, PerfilFuncionario, TipoDocumento, DocumentoFuncionario, EventoLaboral, Evaluacion, BeneficioFuncionario
from django.core.validators import FileExtensionValidator
from .forms import PerfilFuncionarioForm, DocumentoFuncionarioForm, EventoLaboralForm, DocumentoFuncionarioForm, TipoDocumentoForm, EvaluacionForm, BeneficioFuncionarioForm, UsuarioForm, RegistroForm
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
<<<<<<< HEAD
=======
from .models import PerfilFuncionario

>>>>>>> branch-RossNuevo

def test_template(request):
    return render(request, 'auth/login.html')  # prueba directa

    # ------------------------ AUTENTICACIÓN ------------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_inicio')
        else:
            messages.error(request, "Credenciales incorrectas.")
    
    return render(request, 'auth/login.html')

def logout_view(request):
   request.session.flush()
   messages.success(request, "Sesión cerrada correctamente")
   return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                messages.error(request, "Las contraseñas no coinciden.")
            else:
                form.save()
                messages.success(request, "Usuario creado con éxito. Ahora puedes iniciar sesión.")
                return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'auth/signup.html', {'form': form})

    # ------------------------ VISTAS GENERALES ------------------------

@login_required
def menu_inicio(request):
    return render(request, 'menu_inicio.html')

    # ------------------------ FUNCIONARIOS ------------------------

@login_required
def lista_funcionarios(request):
    funcionarios = PerfilFuncionario.objects.all()
    departamentos = PerfilFuncionario.objects.values_list('departamento', flat=True).distinct()
    return render(request, 'funcionarios/lista_funcionarios.html', {
    'funcionarios': funcionarios,
    'departamentos': departamentos
    })

@login_required
def crear_funcionario(request):
    if request.method == 'POST':
        form = PerfilFuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            func = form.save(commit=False)
            if request.POST.get('cargo')=='Otro':
                func.cargo = request.POST.get('otro_cargo','Otro')
            if request.POST.get('departamento')=='Otro':
                func.departamento = request.POST.get('otro_departamento','Otro')
            func.save()
            messages.success(request, "Funcionario registrado correctamente.")
            return redirect('lista_funcionarios')
    else:
        form = PerfilFuncionarioForm()
    return render(request, 'funcionarios/crear_funcionario.html', {'form': form})

@login_required
def editar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(PerfilFuncionario, pk=id_funcionario)
    if request.method == 'POST':
        form = PerfilFuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionario actualizado correctamente.")
            return redirect('lista_funcionarios')
        else:
            form = PerfilFuncionarioForm(instance=funcionario)
        return render(request, 'funcionarios/editar_funcionario.html', {'form': form})

@login_required
def eliminar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(PerfilFuncionario, pk=id_funcionario)
    funcionario.delete()
    messages.success(request, "Funcionario eliminado correctamente.")
    return redirect('lista_funcionarios')

    # ------------------------ DOCUMENTOS ------------------------

def lista_documentos(request):
    documentos = DocumentoFuncionario.objects.select_related('id_funcionario', 'id_tipo_documento').all()
    return render(request, 'documentos/lista_documentos.html', {'documentos': documentos})

<<<<<<< HEAD
def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoFuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Documento registrado correctamente.")
            return redirect('lista_documentos_funcionario')
        else:
            form = DocumentoFuncionarioForm()
        return render(request, 'documentos/crear_documento.html', {'form': form})
=======
from django.shortcuts import render
from django.contrib import messages
from .forms import DocumentoFuncionarioForm
from .models import PerfilFuncionario


def crear_documento(request):
    mostrar_toast = False

    if request.method == 'POST':
        form = DocumentoFuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']

            try:
                funcionario = PerfilFuncionario.objects.get(cedula=cedula)
            except PerfilFuncionario.DoesNotExist:
                messages.error(request, "Funcionario no registrado. Por favor verifique la cédula.")
                return render(request, 'documentos/crear_documento.html', {
                    'form': form,
                    'mostrar_toast': False
                })

            documento = form.save(commit=False)
            documento.id_funcionario = funcionario
            documento.save()
            messages.success(request, "Documento guardado correctamente.")
            return render(request, 'documentos/crear_documento.html', {
                'form': DocumentoFuncionarioForm(),
                'mostrar_toast': True
            })

    else:
        form = DocumentoFuncionarioForm()

    return render(request, 'documentos/crear_documento.html', {
        'form': form
    })

from .models import DocumentoFuncionario, TipoDocumento

def lista_documentos(request):
    tipo = request.GET.get('tipo')
    documentos = DocumentoFuncionario.objects.select_related('id_funcionario', 'id_tipo_documento')

    if tipo:
        documentos = documentos.filter(id_tipo_documento=tipo)

    tipos_documento = TipoDocumento.objects.all()
    return render(request, 'documentos/lista_documentos.html', {
        'documentos': documentos,
        'tipos_documento': tipos_documento
    })


>>>>>>> branch-RossNuevo

def editar_documento(request, id_documento):
    documento = get_object_or_404(DocumentoFuncionario, pk=id_documento)
    if request.method == 'POST':
        form = DocumentoFuncionarioForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            messages.success(request, "Documento actualizado correctamente.")
            return redirect('lista_documentos_funcionario')
        else:
            form = DocumentoFuncionarioForm(instance=documento)
        return render(request, 'documentos/editar_documento.html', {'form': form})

def eliminar_documento(request, id_documento):
    documento = get_object_or_404(DocumentoFuncionario, pk=id_documento)
    documento.delete()
    messages.success(request, "Documento eliminado correctamente.")
    return redirect('lista_documentos_funcionario')
<<<<<<< HEAD
# ------------------------ TIPOS DE DOCUMENTO ------------------------
def lista_tipos_documento(request):
    tipos_documento = TipoDocumento.objects.all()
    return render(request, 'documentos/lista_tipos_documento.html', {'tipos_documento': tipos_documento})
=======


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TipoDocumento
from .forms import TipoDocumentoForm

def lista_tipos_documento(request):
    filtro = request.GET.get('filtro')

    if filtro == 'obligatorios':
        tipos_documento = TipoDocumento.objects.filter(obligatorio=True)
    elif filtro == 'no-obligatorios':
        tipos_documento = TipoDocumento.objects.filter(obligatorio=False)
    else:
        tipos_documento = TipoDocumento.objects.all()

    return render(request, 'documentos/lista_tipos_documento.html', {
        'tipos_documento': tipos_documento,
        'filtro': filtro
    })

    
>>>>>>> branch-RossNuevo

def crear_tipo_documento(request):
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de documento registrado correctamente.")
            return redirect('lista_tipos_documento')
<<<<<<< HEAD
        else:
            form = TipoDocumentoForm()
        return render(request, 'documentos/crear_tipo_documento.html', {'form': form})
    
def editar_tipo_documento(request, id_tipo_documento):
    tipo_documento = get_object_or_404(TipoDocumento, pk=id_tipo_documento)
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST, instance=tipo_documento)
=======
    else:
        form = TipoDocumentoForm()
    return render(request, 'documentos/crear_tipo_documento.html', {'form': form})

def editar_tipo_documento(request, pk):
    tipo = get_object_or_404(TipoDocumento, pk=pk)
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST, instance=tipo)
>>>>>>> branch-RossNuevo
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de documento actualizado correctamente.")
            return redirect('lista_tipos_documento')
<<<<<<< HEAD
        else:
            form = TipoDocumentoForm(instance=tipo_documento)
        return render(request, 'documentos/editar_tipo_documento.html', {'form': form})
    
def eliminar_tipo_documento(request, id_tipo_documento):
    tipo_documento = get_object_or_404(TipoDocumento, pk=id_tipo_documento)
    tipo_documento.delete()
    messages.success(request, "Tipo de documento eliminado correctamente.")
    return redirect('lista_tipos_documento')

=======
    else:
        form = TipoDocumentoForm(instance=tipo)
    return render(request, 'documentos/crear_tipo_documento.html', {'form': form})

def eliminar_tipo_documento(request, pk):
    tipo = get_object_or_404(TipoDocumento, pk=pk)
    tipo.delete()
    messages.success(request, "Tipo de documento eliminado correctamente.")
    return redirect('lista_tipos_documento')


>>>>>>> branch-RossNuevo
# ------------------------ EVALUACIONES ------------------------

def lista_evaluaciones(request):
    evaluaciones = Evaluacion.objects.select_related('id_funcionario').all()
    return render(request, 'evaluaciones/lista_evaluaciones.html', {'evaluaciones': evaluaciones})

def crear_evaluacion(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evaluación registrada correctamente.")
            return redirect('lista_evaluaciones')
        else:
            form = EvaluacionForm()
        return render(request, 'evaluaciones/crear_evaluacion.html', {'form': form})
    
def editar_evaluacion(request, id_evaluacion):
    evaluacion = get_object_or_404(Evaluacion, pk=id_evaluacion)
    if request.method == 'POST':
        form = EvaluacionForm(request.POST, instance=evaluacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Evaluación actualizada correctamente.")
            return redirect('lista_evaluaciones')
        else:
            form = EvaluacionForm(instance=evaluacion)
        return render(request, 'evaluaciones/editar_evaluacion.html', {'form': form})
    
def eliminar_evaluacion(request, id_evaluacion):
    evaluacion = get_object_or_404(Evaluacion, pk=id_evaluacion)
    evaluacion.delete()
    messages.success(request, "Evaluación eliminada correctamente.")
    return redirect('lista_evaluaciones')

# ------------------------ BENEFICIOS ------------------------

def lista_beneficios(request):
    beneficios = BeneficioFuncionario.objects.select_related('id_funcionario').all()
    return render(request, 'beneficios/lista_beneficios.html', {'beneficios': beneficios})

def crear_beneficio(request):
    if request.method == 'POST':
<<<<<<< HEAD
        form = BeneficioFuncionarioForm(request.POST)
=======
        form = BeneficioFuncionarioForm(request.POST, request.FILES)
>>>>>>> branch-RossNuevo
        if form.is_valid():
            form.save()
            messages.success(request, "Beneficio registrado correctamente.")
            return redirect('lista_beneficios')
<<<<<<< HEAD
        else:
            form = BeneficioFuncionarioForm()
        return render(request, 'beneficios/crear_beneficio.html', {'form': form})
=======
    else:
        form = BeneficioFuncionarioForm()

    funcionarios = PerfilFuncionario.objects.all()
    return render(request, 'beneficios/crear_beneficio.html', {'form': form, 'funcionarios': funcionarios})


>>>>>>> branch-RossNuevo
    
def editar_beneficio(request, id_beneficio):
    beneficio = get_object_or_404(BeneficioFuncionario, pk=id_beneficio)
    if request.method == 'POST':
        form = BeneficioFuncionarioForm(request.POST, instance=beneficio)
        if form.is_valid():
            form.save()
            messages.success(request, "Beneficio actualizado correctamente.")
            return redirect('lista_beneficios')
        else:
            form = BeneficioFuncionarioForm(instance=beneficio)
        return render(request, 'beneficios/editar_beneficio.html', {'form': form})
    
def eliminar_beneficio(request, id_beneficio):
    beneficio = get_object_or_404(BeneficioFuncionario, pk=id_beneficio)
    beneficio.delete()
    messages.success(request, "Beneficio eliminado correctamente.")
    return redirect('lista_beneficios')

# ------------------------ EVENTOS FUNCIONARIOS ------------------------
<<<<<<< HEAD

def lista_eventos_funcionario(request):
    eventos = EventoLaboral.objects.select_related('id_funcionario').all()
    return render(request, 'eventos/lista_eventos_funcionario.html', {'eventos': eventos})

def registrar_evento_funcionario(request):
    if request.method == 'POST':
        form = EventoLaboralForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento registrado exitosamente.")
            return redirect('lista_eventos_funcionario')
        else:
            form = EventoLaboralForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})
=======
def lista_eventos(request):
    eventos = EventoLaboral.objects.select_related('id_funcionario').all()
    return render(request, 'eventos/lista_eventos_funcionario.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoLaboralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento registrado exitosamente.")
            return redirect('lista_eventos')
    else:
        form = EventoLaboralForm()

    funcionarios = PerfilFuncionario.objects.all()
    return render(request, 'eventos/crear_evento.html', {'form': form, 'funcionarios': funcionarios})


>>>>>>> branch-RossNuevo

def editar_evento(request, id_evento):
    evento = get_object_or_404(EventoLaboral, pk=id_evento)
    if request.method == 'POST':
        form = EventoLaboralForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento actualizado correctamente.")
            return redirect('lista_eventos_funcionario')
<<<<<<< HEAD
        else:
            form = EventoLaboralForm(instance=evento)
        return render(request, 'eventos/editar_evento.html', {'form': form})
=======
    else:
        form = EventoLaboralForm(instance=evento)
    
    funcionarios = PerfilFuncionario.objects.all()
    return render(request, 'eventos/editar_evento.html', {'form': form, 'funcionarios': funcionarios})

>>>>>>> branch-RossNuevo
    
def eliminar_evento(request, id_evento):
    evento = get_object_or_404(EventoLaboral, pk=id_evento)
    evento.delete()
    messages.success(request, "Evento eliminado correctamente.")
<<<<<<< HEAD
    return redirect('lista_eventos_funcionario')
=======
    return redirect('lista_eventos')


>>>>>>> branch-RossNuevo

#-------------------------- USUARIOS --------------------------

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password_claro = request.POST['password']
        password_hash = make_password(password_claro)
        rol = request.POST['rol']

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
        else:
            usuario = Usuario.objects.create(username=username, password=password_hash, rol=rol)
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(User, pk=id_usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente.")
            return redirect('lista_usuarios')
        else:
            form = UsuarioForm(instance=usuario)
        return render(request, 'tasks/editar_usuario.html', {'form': form})
    
def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    usuario.delete()
    messages.success(request, "Usuario eliminado correctamente.")
    return redirect('lista_usuarios')

# ------------------------ PERMISOS ------------------------
def is_admin(user):
    return user.rol == 'admin'
def is_user(user):
    return user.rol == 'user'
<<<<<<< HEAD
=======

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DocumentoFuncionarioForm

def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoFuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Documento registrado correctamente.")
            return redirect('lista_documentos_funcionario')
    else:
        form = DocumentoFuncionarioForm()
    
    return render(request, 'documentos/crear_documento.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DocumentoFuncionarioForm
from .models import PerfilFuncionario, DocumentoFuncionario

def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoFuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            try:
                funcionario = PerfilFuncionario.objects.get(cedula=cedula)
            except PerfilFuncionario.DoesNotExist:
                messages.error(request, "El funcionario con cédula ingresada no existe. Por favor registre primero al funcionario.")
                return redirect('crear_funcionario')  # Ajustá si tu vista se llama distinto

            documento = form.save(commit=False)
            documento.id_funcionario = funcionario
            documento.save()
            messages.success(request, "Documento registrado correctamente.")
            return redirect('lista_documentos_funcionario')
    else:
        form = DocumentoFuncionarioForm()

    return render(request, 'documentos/crear_documento.html', {'form': form})

>>>>>>> branch-RossNuevo
