from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clientes'),
    path('crearClientes', views.crearCliente, name='crear_clientes'),
    path('modificarCliente/<int:cedula>/', views.modificarCliente, name='modificar_cliente'),
    path('eliminarCliente/<int:cedula>/', views.eliminarCliente, name='eliminar_cliente'),

    path('cuentas/<int:cedula>/', views.listarCuentas, name="cuentas"),
    path('crearCuentas/<int:cedula>/', views.crearCuenta, name='crear_cuentas'),
    path('modificarCuenta/<int:numero>/<int:cedula>/', views.modificarCuenta, name='modificar_cuenta'),
    path('eliminarCuenta/<int:numero>/<int:cedula>/', views.eliminarCuenta, name='eliminar_cuenta'),
]

