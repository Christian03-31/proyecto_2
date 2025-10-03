from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserVeterinaria(AbstractUser):
    es_trabajador = models.BooleanField(default=False)
    es_cliente = models.BooleanField(default=False)

class Cita(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    rut_propietario = models.CharField(max_length=12)
    tipo_mascota = models.CharField(max_length=20)
    nombre_mascota = models.CharField(max_length=100)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()

    def __str__(self):
        return f"{self.nombre_mascota} ({self.fecha_cita} a las {self.hora_cita})"
