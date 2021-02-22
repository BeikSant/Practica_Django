from django.urls import path

from . import views

urlpatterns = [
    path('', views.autenticar, name='autenticar'),
    path('desactivado', views.desactivado, name='no_activo'),
    path('welcome', views.welcome, name='welcome'),
]
