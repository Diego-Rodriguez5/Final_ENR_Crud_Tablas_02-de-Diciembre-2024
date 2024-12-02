from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.

def inicio_vistaProveedores(request):
    losproveedores=Proveedores.objects.all()
    return render(request,"gestionarProveedores.html", {"misproveedores":losproveedores}   )

def registrarProveedores(request):
    idProveedores=request.POST["txtidProveedores"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    tipoProducto=request.POST["txttipoProducto"]
    paisOrigen=request.POST["txtpaisOrigen"]
    estado=request.POST["txtestado"]
    ciudad=request.POST["txtciudad"]
    codigoPostal=request.POST["txtcodigoPostal"]

    guardarproveedores=Proveedores.objects.create(
    idProveedores=idProveedores, nombre=nombre, direccion=direccion, telefono=telefono, correo=correo, tipoProducto=tipoProducto, paisOrigen=paisOrigen, estado=estado, ciudad=ciudad, codigoPostal=codigoPostal
    ) #GUARDA EL REGISTRO

    return redirect("proveedores")

def seleccionarProveedores(request, idProveedores):
    provedor=Proveedores.objects.get(idProveedores=idProveedores)
    return render(request,"editarProveedores.html",{"misproveedores":provedor})

def editarProveedores(request):
    idProveedores=request.POST["txtidProveedores"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    tipoProducto=request.POST["txttipoProducto"]
    paisOrigen=request.POST["txtpaisOrigen"]
    estado=request.POST["txtestado"]
    ciudad=request.POST["txtciudad"]
    codigoPostal=request.POST["txtcodigoPostal"]
    provedor=Proveedores.objects.get(idProveedores=idProveedores)
    provedor.nombre=nombre
    provedor.direccion=direccion
    provedor.telefono=telefono
    provedor.correo=correo
    provedor.tipoProducto=tipoProducto
    provedor.paisOrigen=paisOrigen
    provedor.estado=estado
    provedor.ciudad=ciudad
    provedor.codigoPostal=codigoPostal
    provedor.save() # guardar registro actualizado
    return redirect("proveedores")

def borrarProveedores(request, idProveedores):
    provedor=Proveedores.objects.get(idProveedores=idProveedores)
    provedor.delete() # borrar el registro
    return redirect("proveedores")
