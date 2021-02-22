
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="transacciones"),
    path('cuenta/<int:numero>/', views.getCuentaPorCliente, name="cuenta_cliente"),
    path('depositar/<int:numero>/', views.depositar, name="depositar"),
    path('retirar/<int:numero>/', views.retirar, name="retirar"),
]