from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PerfilFuncionario
from django.contrib import messages
from .models import TipoDocumento, DocumentoFuncionario
from .forms import TipoDocumentoForm, DocumentoFuncionarioForm
from django.shortcuts import render

def menu_inicio(request):
    return render(request, 'tasks/menu_inicio.html')


def lista_funcionarios(request):
    funcionarios = PerfilFuncionario.objects.all()
    departamentos = PerfilFuncionario.objects.values_list('departamento', flat=True).distinct()
    context = {
        'funcionarios': funcionarios,
        'departamentos': departamentos,
    }
    return render(request, 'tasks/lista_funcionarios.html', {'funcionarios': funcionarios})

@login_required
@user_passes_test(lambda u: u.is_staff)  # Solo administradores
def editar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(PerfilFuncionario, id_funcionario=id_funcionario)
    
    if request.method == 'POST':
        form = actualizar_funcionario(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = actualizar_funcionario(instance=funcionario)
    
    context = {
        'form': form,
        'funcionario': funcionario
    }
    return render(request, 'editar_funcionario.html', context)
    
#Editar si es admin
@login_required
@user_passes_test(lambda u: u.is_staff)  # Solo administradores
def eliminar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(PerfilFuncionario, id_funcionario=id_funcionario)
    funcionario.delete()
    return redirect('lista_funcionarios')



def crear_funcionario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')

        cargo = request.POST.get('cargo')
        otro_cargo = request.POST.get('otro_cargo')
        if cargo == 'Otro' and otro_cargo:
            cargo = otro_cargo

        departamento = request.POST.get('departamento')
        otro_departamento = request.POST.get('otro_departamento')
        if departamento == 'Otro' and otro_departamento:
            departamento = otro_departamento

        fecha_ingreso = request.POST.get('fecha_ingreso')
        estado = request.POST.get('estado')
        estado_civil = request.POST.get('estado_civil')

        funcionario = PerfilFuncionario(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            cargo=cargo,
            fecha_ingreso=fecha_ingreso,
            departamento=departamento,
            estado=estado,
            estado_civil=estado_civil
        )
        funcionario.save()

        messages.success(request, '¡Funcionario creado exitosamente! ✅')
        return redirect('lista_funcionarios')

    return render(request, 'tasks/crear_funcionario.html')

def actualizar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(PerfilFuncionario, id_funcionario=id_funcionario)

    if request.method == 'POST':
        funcionario.nombre = request.POST.get('nombre')
        funcionario.apellido = request.POST.get('apellido')
        funcionario.cedula = request.POST.get('cedula')

        cargo = request.POST.get('cargo')
        otro_cargo = request.POST.get('otro_cargo')
        if cargo == 'Otro' and otro_cargo:
            funcionario.cargo = otro_cargo
        else:
            funcionario.cargo = cargo

        departamento = request.POST.get('departamento')
        otro_departamento = request.POST.get('otro_departamento')
        if departamento == 'Otro' and otro_departamento:
            funcionario.departamento = otro_departamento
        else:
            funcionario.departamento = departamento

        funcionario.fecha_ingreso = request.POST.get('fecha_ingreso')
        funcionario.estado = request.POST.get('estado')
        funcionario.estado_civil = request.POST.get('estado_civil')

        funcionario.save()

        messages.success(request, '¡Funcionario actualizado exitosamente! ✏️')
        return redirect('lista_funcionarios')

    return render(request, 'tasks/actualizar_funcionario.html', {'funcionario': funcionario})

def eliminar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(PerfilFuncionario, id_funcionario=id_funcionario)
    funcionario.delete()

    messages.success(request, '¡Funcionario eliminado exitosamente! 🗑️')
    return redirect('lista_funcionarios')

# ---------------- TIPO DOCUMENTO ----------------

def lista_tipos_documento(request):
    tipos = TipoDocumento.objects.all()
    return render(request, 'tasks/lista_tipos_documento.html', {'tipos': tipos})

def crear_tipo_documento(request):
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tipos_documento')
    else:
        form = TipoDocumentoForm()
    return render(request, 'tasks/crear_tipo_documento.html', {'form': form})

# ---------------- DOCUMENTOS FUNCIONARIOS ----------------

def lista_documentos(request):
    documentos = DocumentoFuncionario.objects.select_related('id_funcionario', 'id_tipo_documento').all()
    return render(request, 'tasks/lista_documentos.html', {'documentos': documentos})



def crear_documento(request):
    if request.method == 'POST':
        form = DocumentoFuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_documentos_funcionario')
    else:
        form = DocumentoFuncionarioForm()
    return render(request, 'tasks/crear_documento.html', {'form': form})