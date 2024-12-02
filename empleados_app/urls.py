from django.urls import path
from empleados_app import views
urlpatterns = [
    path("empleados", views.inicio_vistaEmpleados, name= "empleados" ),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path("seleccionarEmpleados/<idEmpleados>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
    path("borrarEmpleados/<idEmpleados>", views.borrarEmpleados,name="borrarEmpleados"),
    
]
