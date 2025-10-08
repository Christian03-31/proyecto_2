from rest_framework import serializers
from .models import Cita, UserVeterinaria

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ('nombre_propietario',
                    'rut_propietario', 
                    'tipo_mascota',
                    'nombre_mascota',
                    'fecha_cita',
                    'hora_cita',
                    'propietario'
                )
        read_only_fields=('nombre_propietario',
                    'rut_propietario', 
                    'tipo_mascota',
                    'nombre_mascota',
                    'fecha_cita',
                    'hora_cita',
                    'propietario'
                )
