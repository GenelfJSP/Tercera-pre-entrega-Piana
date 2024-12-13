from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)
    compras = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre_usuario}"

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_proveedor


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto