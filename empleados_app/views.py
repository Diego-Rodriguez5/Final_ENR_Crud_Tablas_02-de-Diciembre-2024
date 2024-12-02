from django.shortcuts import render, redirect
from .models import Empleados

# Create your views here.

def inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html", {"misempleados":losempleados}   )

def registrarEmpleados(request):
    idEmpleados=request.POST["txtidEmpleados"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    cargo=request.POST["txtcargo"]
    fechaContratacion=request.POST["datecontacto"]
    telefono=request.POST["txttelefono"]
    salario=request.POST["txtsalario"]

    guardarempleados=Empleados.objects.create(
    idEmpleados=idEmpleados, nombre=nombre, apellido=apellido, cargo=cargo, fechaContratacion=fechaContratacion, telefono=telefono, salario=salario
    ) #GUARDA EL REGISTRO

    return redirect("empleados")

def seleccionarEmpleados(request, idEmpleados):
    empleado=Empleados.objects.get(idEmpleados=idEmpleados)
    return render(request,"editarEmpleados.html",{"misempleados":empleado})

def editarEmpleados(request):
    idEmpleados=request.POST["txtidEmpleados"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    cargo=request.POST["txtcargo"]
    fechaContratacion=request.POST["datecontacto"]
    telefono=request.POST["txttelefono"]
    salario=request.POST["txtsalario"]
    empleado=Empleados.objects.get(idEmpleados=idEmpleados)
    empleado.nombre=nombre
    empleado.apellido=apellido
    empleado.cargo=cargo
    empleado.fechaContratacion=fechaContratacion
    empleado.telefono=telefono
    empleado.salario=salario
    empleado.save() # guardar registro actualizado
    return redirect("empleados")

def borrarEmpleados(request, idEmpleados):
    empleado=Empleados.objects.get(idEmpleados=idEmpleados)
    empleado.delete() # borrar el registro
    return redirect("empleados")