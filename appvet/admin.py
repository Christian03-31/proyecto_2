from django.contrib import admin
from .models import UserVeterinaria, Cita
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Cita)

class UserVeterinariaAdmin(UserAdmin):
    model = UserVeterinaria
    list_display = ['username', 'email', 'is_staff', 'es_trabajador', 'es_cliente']
    list_filter = ['is_staff', 'es_trabajador', 'es_cliente']
    search_fields = ['username', 'email']
    ordering = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'es_trabajador', 'es_cliente')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'es_trabajador', 'es_cliente'),
        }),
    )

admin.site.register(UserVeterinaria, UserVeterinariaAdmin)