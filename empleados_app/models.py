from django.db import models

# Create your models here.
class Empleados(models.Model):
    idEmpleados=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50)
    fechaContratacion=models.DateField(null=False,blank=False)
    telefono=models.CharField(max_length=15)
    salario=models.FloatField()

    def __str__(self):
        return self.nombre