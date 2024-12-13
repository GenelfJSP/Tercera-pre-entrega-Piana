from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor/<int:proveedor_id>/productos/', views.productos_por_proveedor, name='productos_por_proveedor'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('buscar_proveedor/', views.buscar_proveedor, name='buscar_proveedor'),
    path('productos/', views.productos, name='productos'),
]
