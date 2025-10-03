from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Pedido/', views.pagpedir_hora, name='pedir'),
    path('Paciente/', views.pagpaciente, name='paciente'),
    path('Trabajadores/', views.pagtrabajadores, name='trabajador'),
    path('Admin/', views.pagadmin),
    path('Revisar/', views.pagrev_hora, name='revisar'),
    path('admin/', views.login_admin, name='login_admin'),
    path('login_paciente/', views.login_paciente, name='login_paciente'),
    path('login_trabajador/', views.login_trabajador, name='login_trabajador'),
    path('logout_paciente/', views.logout_PACIENTE, name='logoutP'),
    path('logout_trabajador/', views.logout_trabajador, name='logoutT'),


]