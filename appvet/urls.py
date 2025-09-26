from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Pedido/', views.pagpedir_hora),
    path('Paciente/', views.pagpaciente),
    path('Trabajadores/', views.pagtrabajadores),
    path('Admin/', views.pagadmin),
    path('Revisar/', views.pagrev_hora),

]