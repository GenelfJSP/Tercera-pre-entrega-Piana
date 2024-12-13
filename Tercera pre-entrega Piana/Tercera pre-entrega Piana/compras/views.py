from .models import Usuario
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RestablecerContraseñaForm
from django.shortcuts import render, redirect
from .forms import ClienteForm, BuscarClienteForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}!')
            return redirect('iniciar_sesion')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = UserCreationForm()
    return render(request, 'registrar_usuario.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Has iniciado sesión correctamente')
                return redirect('usuarios')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Ingreselo correctamente')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def listar_proveedores(request):
    print("Se está cargando la vista del listado de proveedores")
    proveedores = Proveedor.objects.all()
    return render(request, 'compras/listar_proveedores.html', {'proveedores': proveedores})

def inicio(request):
    print("Se está cargando la vista de inicio")
    return render(request, 'inicio.html')

def buscar_proveedor(request):
    print("Buscando proveedor...")
    proveedores = Proveedor.objects.all()
    return render(request, 'compras/buscar_proveedor.html', {'proveedores': proveedores})

def usuarios(request):
    print("Se está cargando la vista de usuarios")
    return render(request, 'compras/usuarios.html')

def productos(request):
    print("Se está cargando la vista de productos")
    return render(request, 'compras/productos.html')

def productos_por_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    productos = Producto.objects.filter(proveedor=proveedor)
    return render(request, 'compras/productos_por_proveedor.html', {'proveedor': proveedor, 'productos': productos})

def listar_usuarios(request):
    usuarios = User.objects.all()
    print("Se está cargando la vista de los usuarios")
    return render(request, 'compras/listar_usuarios.html', {'usuarios': usuarios})

def reestablecimiento_contraseña(request):
    if request.method == "POST":
        form = UsernameResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                token = default_token_generator.make_token(user)
                reset_url = request.build_absolute_uri(reverse('RestablecerContraseña', args=[user.pk, token]))
                send_mail(
                    "Restablece tu contraseña",
                    f"Para restablecer tu contraseña, haz clic en el siguiente enlace: {reset_url}",
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )
                messages.success(request, "Te hemos enviado un enlace para restablecer tu contraseña.")
                return redirect('iniciar_sesion')
            except User.DoesNotExist:
                messages.error(request, "El nombre de usuario no existe.")
    else:
        form = RestablecerContraseñaForm()
    return render(request, 'reestablecimiento_contraseña.html', {'form': form})

def restablecer_contraseña(request):
    return render(request, 'restablecer_contraseña.html')
