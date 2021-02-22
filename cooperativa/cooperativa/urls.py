from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.gestion_clientes.urls')),
    path('login/', include('apps.login.urls')),
    path('', views.index, name='homepage'),
    path('transacciones/', include('apps.transacciones.urls')),
]
