from django.contrib import admin

from apps.modelo.models import Cliente
from apps.modelo.models import Cuenta

class AdminCliente(admin.ModelAdmin):
    list_display = ('cedula','apellidos','nombres','correo','celular')
    list_editable = ('correo','celular')
    list_filter = ('nombres','estadoCivil')
    search_fields = ('nombres','apellidos','cedula')

    class Meta:
        model = Cliente

admin.site.register(Cliente, AdminCliente)


class AdminCuenta(admin.ModelAdmin):
    list_display = ('numero','saldo','tipoCuenta','estado')
    list_filter = ('tipoCuenta','estado','cliente')
    search_fields = ['numero']

    class Meta:
        model = Cuenta

admin.site.register(Cuenta, AdminCuenta)
