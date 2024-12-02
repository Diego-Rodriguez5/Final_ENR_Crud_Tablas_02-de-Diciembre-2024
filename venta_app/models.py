from django.db import models

# Create your models here.

class Venta(models.Model):
    idVenta=models.CharField(primary_key=True, max_length=20)
    fechaVenta=models.DateField(null=False,blank=False)
    total=models.FloatField()
    idCliente=models.PositiveIntegerField()
    idEmpleado=models.PositiveIntegerField()
    tipoPago=models.CharField(max_length=20)
    descuento=models.FloatField()
    idProducto=models.PositiveIntegerField()
    cantidad=models.CharField(max_length=500)

    def __str__(self):
        return self.cantidad