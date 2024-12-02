from django.shortcuts import render, redirect
from .models import Productos
# Create your views here.

def inicio_vistaProductos(request):
    losproductos=Productos.objects.all()
    return render(request,"gestionarProductos.html", {"misproductos":losproductos}   )

def registrarProductos(request):
    idProductos=request.POST["txtidProductos"]
    nombre=request.POST["txtnombre"]
    categoria=request.POST["txtcategoria"]
    precio=request.POST["txtprecio"]
    stock=request.POST["txtstock"]
    fechaCaducidad=request.POST["datecaducidad"]
    descripcion=request.POST["txtdescripcion"]
    idSucursal=request.POST["numidsucursal"]
    idProveedor=request.POST["numidproveedor"]

    guardarproductos=Productos.objects.create(
    idProductos=idProductos, nombre=nombre, categoria=categoria, precio=precio, stock=stock, fechaCaducidad=fechaCaducidad, descripcion=descripcion, idSucursal=idSucursal, idProveedor=idProveedor
    ) #GUARDA EL REGISTRO

    return redirect("productos")

def seleccionarProductos(request, idProductos):
    producto=Productos.objects.get(idProductos=idProductos)
    return render(request,"editarProductos.html",{"misproductos":producto})

def editarProductos(request):
    idProductos=request.POST["txtidProductos"]
    nombre=request.POST["txtnombre"]
    categoria=request.POST["txtcategoria"]
    precio=request.POST["txtprecio"]
    stock=request.POST["txtstock"]
    fechaCaducidad=request.POST["datecaducidad"]
    descripcion=request.POST["txtdescripcion"]
    idSucursal=request.POST["numidsucursal"]
    idProveedor=request.POST["numidproveedor"]
    producto=Productos.objects.get(idProductos=idProductos)
    producto.nombre=nombre
    producto.categoria=categoria
    producto.precio=precio
    producto.stock=stock
    producto.fechaCaducidad=fechaCaducidad
    producto.descripcion=descripcion
    producto.idSucursal=idSucursal
    producto.idProveedor=idProveedor
    producto.save() # guardar registro actualizado
    return redirect("productos")

def borrarProductos(request, idProductos):
    producto=Productos.objects.get(idProductos=idProductos)
    producto.delete() # borrar el registro
    return redirect("productos")