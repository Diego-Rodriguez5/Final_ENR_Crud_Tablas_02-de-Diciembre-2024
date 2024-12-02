from django.db import models
# Create your models here.

class Productos(models.Model):
    idProductos=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=30)
    precio=models.FloatField()
    stock=models.CharField(max_length=100)
    fechaCaducidad=models.DateField(null=False,blank=False)
    descripcion=models.CharField(max_length=100)
    idSucursal=models.PositiveIntegerField()
    idProveedor=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre