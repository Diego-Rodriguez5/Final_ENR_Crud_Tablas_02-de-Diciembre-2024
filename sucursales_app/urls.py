from django.urls import path
from sucursales_app import views
urlpatterns = [
    path("sucursales", views.inicio_vistaSucursales, name= "sucursales" ),
    path("registrarSucursales/",views.registrarSucursales,name="registrarSucursales"),
    path("seleccionarSucursales/<idSucursales>",views.seleccionarSucursales,name="seleccionarSucursales"),
    path("editarSucursales/",views.editarSucursales,name="editarSucursales"),
    path("borrarSucursales/<idSucursales>", views.borrarSucursales,name="borrarSucursales"),
    
]
