from django.urls import path
from proveedores_app import views
urlpatterns = [
    path("proveedores", views.inicio_vistaProveedores, name= "proveedores" ),
    path("registrarProveedores/",views.registrarProveedores,name="registrarProveedores"),
    path("seleccionarProveedores/<idProveedores>",views.seleccionarProveedores,name="seleccionarProveedores"),
    path("editarProveedores/",views.editarProveedores,name="editarProveedores"),
    path("borrarProveedores/<idProveedores>", views.borrarProveedores,name="borrarProveedores"),
    
]
