from apps.modelo.models import Cliente, Cuenta
from .forms import FormularioCliente, FormularioCuenta
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        #manejo del ORM
        listaClientes = Cliente.objects.all()
        return render (request, 'clientes/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def crearCliente(request):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        formulario_cliente = FormularioCliente(request.POST)
        formulario_cuenta = FormularioCuenta(request.POST)
        if request.method == 'POST':
            if formulario_cliente.is_valid() and formulario_cuenta.is_valid():

                cliente = Cliente()
                datos_cliente = formulario_cliente.cleaned_data
                cliente.cedula = datos_cliente.get('cedula')
                cliente.nombres = datos_cliente.get('nombres')
                cliente.apellidos = datos_cliente.get('apellidos')
                cliente.genero = datos_cliente.get('genero')
                cliente.estadoCivil = datos_cliente.get('estadoCivil')
                cliente.correo = datos_cliente.get('correo')
                cliente.telefono = datos_cliente.get('telefono')
                cliente.celular = datos_cliente.get('celular')
                cliente.direccion = datos_cliente.get('direccion')
                #ORM
                cliente.save()

                cuenta = Cuenta()
                datos_cuenta = formulario_cuenta.cleaned_data
                cuenta.numero = datos_cuenta.get('numero')
                cuenta.saldo = datos_cuenta.get('saldo')
                cuenta.tipoCuenta = datos_cuenta.get('tipoCuenta')
                cuenta.cliente = cliente
                #ORM
                cuenta.save()

                user = User.objects.create_user(cliente.cedula, cliente.correo, cliente.cedula)
                user.first_name = cliente.nombres
                user.last_name = cliente.apellidos
                grupo = Group.objects.get(name='clientes')
                user.groups.add(grupo)
                user.save()

            return redirect(index)
        return render (request, 'clientes/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def modificarCliente(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        cliente = Cliente.objects.get(cedula=cedula)
        if request.method == 'GET':
            formulario_cliente = FormularioCliente(instance = cliente)
        else:
            formulario_cliente = FormularioCliente(request.POST, instance = cliente)
            if formulario_cliente.is_valid():
                #ORM
                formulario_cliente.save()
            return redirect(index)
        return render (request, 'clientes/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def eliminarCliente(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        cliente = Cliente.objects.get(cedula=cedula)
        cliente.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())
    
@login_required
def listarCuentas(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        cliente = Cliente.objects.get(cedula=cedula)
        cuentas = Cuenta.objects.filter(cliente=cliente)
        return render(request, 'cuentas/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
    
@login_required
def crearCuenta(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        formulario_cuenta = FormularioCuenta(request.POST)
        cliente = Cliente.objects.get(cedula=cedula)
        if request.method == 'POST':
            if formulario_cuenta.is_valid():
                cuenta = Cuenta()
                datos_cuenta = formulario_cuenta.cleaned_data
                cuenta.numero = datos_cuenta.get('numero')
                cuenta.saldo = datos_cuenta.get('saldo')
                cuenta.tipoCuenta = datos_cuenta.get('tipoCuenta')
                cuenta.cliente = cliente
                #ORM
                cuenta.save()
            return redirect(listarCuentas,cedula)
        return render (request, 'cuentas/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
    
@login_required
def modificarCuenta(request, numero, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        cuenta = Cuenta.objects.get(numero=numero)
        if request.method == 'GET':
            formulario_cuenta = FormularioCuenta(instance = cuenta)
        else:
            formulario_cuenta = FormularioCuenta(request.POST, instance = cuenta)
            if formulario_cuenta.is_valid():
                #ORM
                formulario_cuenta.save()
            return redirect(listarCuentas,cedula)
        return render (request, 'cuentas/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
    
@login_required
def eliminarCuenta(request, numero, cedula):
    usuario = request.user
    if usuario.groups.filter(name='gestion_clientes').exists():
        cuenta = Cuenta.objects.get(numero=numero)
        cuenta.delete()
        return redirect(listarCuentas,cedula)
    else:
        return render(request, 'login/forbidden.html', locals())
    
