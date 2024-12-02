from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def inicio_vistaClientes(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarClientes.html", {"misclientes":losclientes}   )

def registrarClientes(request):
    idCliente=request.POST["txtidCliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    fechaRegistro=request.POST["dateregistro"]

    guardarcliente=Cliente.objects.create(
    idCliente=idCliente, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, correo=correo, fechaRegistro=fechaRegistro
    ) #GUARDA EL REGISTRO

    return redirect("clientes")

def seleccionarClientes(request, idCliente):
    cliente=Cliente.objects.get(idCliente=idCliente)
    return render(request,"editarClientes.html",{"misclientes":cliente})

def editarClientes(request):
    idCliente=request.POST["txtidCliente"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    fechaRegistro=request.POST["dateregistro"]
    cliente=Cliente.objects.get(idCliente=idCliente)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.direccion=direccion
    cliente.telefono=telefono
    cliente.correo=correo
    cliente.fechaRegistro=fechaRegistro

    cliente.save() # guardar registro actualizado
    return redirect("clientes")

def borrarClientes(request, idCliente):
    cliente=Cliente.objects.get(idCliente=idCliente)
    cliente.delete() # borrar el registro
    return redirect("clientes")