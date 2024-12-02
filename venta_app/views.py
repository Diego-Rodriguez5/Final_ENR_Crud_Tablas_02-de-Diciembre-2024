from django.shortcuts import render, redirect
from .models import Venta

# Create your views here.

def inicio_vistaVenta(request):
    lasventa=Venta.objects.all()
    return render(request,"gestionarVenta.html", {"misventa":lasventa}   )

def registrarVenta(request):
    idVenta=request.POST["txtidVenta"]
    fechaVenta=request.POST["dateventa"]
    total=request.POST["txttotal"]
    idCliente=request.POST["txtidCliente"]
    idEmpleado=request.POST["txtidEmpleado"]
    tipoPago=request.POST["txttipoPago"]
    descuento=request.POST["txtdescuento"]
    idProducto=request.POST["txtidProducto"]
    cantidad=request.POST["txtcantidad"]

    guardarventa=Venta.objects.create(
    idVenta=idVenta, fechaVenta=fechaVenta, total=total, idCliente=idCliente, idEmpleado=idEmpleado, tipoPago=tipoPago, descuento=descuento, idProducto=idProducto, cantidad=cantidad
    ) #GUARDA EL REGISTRO

    return redirect("venta")

def seleccionarVenta(request, idVenta):
    venta=Venta.objects.get(idVenta=idVenta)
    return render(request,"editarVenta.html",{"misventa":venta})

def editarVenta(request):
    idVenta=request.POST["txtidVenta"]
    fechaVenta=request.POST["dateventa"]
    total=request.POST["txttotal"]
    idCliente=request.POST["txtidCliente"]
    idEmpleado=request.POST["txtidEmpleado"]
    tipoPago=request.POST["txttipoPago"]
    descuento=request.POST["txtdescuento"]
    idProducto=request.POST["txtidProducto"]
    cantidad=request.POST["txtcantidad"]
    venta=Venta.objects.get(idVenta=idVenta)
    venta.fechaVenta=fechaVenta
    venta.total=total
    venta.idCliente=idCliente
    venta.idEmpleado=idEmpleado
    venta.tipoPago=tipoPago
    venta.descuento=descuento
    venta.idProducto=idProducto
    venta.cantidad=cantidad
    venta.save() # guardar registro actualizado
    return redirect("venta")

def borrarVenta(request, idVenta):
    venta=Venta.objects.get(idVenta=idVenta)
    venta.delete() # borrar el registro
    return redirect("venta")