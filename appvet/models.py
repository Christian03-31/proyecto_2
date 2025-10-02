from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserVeterinaria(AbstractUser):
    es_trabajador = models.BooleanField(default=False)
    es_cliente = models.BooleanField(default=False)