from django.db import models

# Create your models here.
class Proveedores(models.Model):
    idProveedores=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=50)
    tipoProducto=models.CharField(max_length=30)
    paisOrigen=models.CharField(max_length=30)
    estado=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    codigoPostal=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre