from django.urls import path
from clientes_app import views
urlpatterns = [
    path("clientes", views.inicio_vistaClientes, name= "clientes" ),
    path("registrarClientes/",views.registrarClientes,name="registrarClientes"),
    path("seleccionarClientes/<idCliente>",views.seleccionarClientes,name="seleccionarClientes"),
    path("editarClientes/",views.editarClientes,name="editarClientes"),
    path("borrarClientes/<idCliente>", views.borrarClientes,name="borrarClientes"),
    
]
