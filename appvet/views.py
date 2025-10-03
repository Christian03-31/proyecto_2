from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from .models import Cita




#Esta seccion es para iniciar sesion
def login_admin(request):
    return redirect(request, '/admin')



def login_trabajador(request):
    if request.method == 'GET':
        print("GET")
        return render(request, 'logins/login_trabajador.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.es_trabajador:
            login(request, user)
            return redirect('trabajador')
        elif user is not None and user.es_cliente:
            print("Usuario existe y es cliente")
            return redirect('login_paciente')
        (request, 'logins/login_trabajador.html')



def login_paciente(request):
    if request.method == 'GET':
        print("GET")
        return render(request, 'logins/login_paciente.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.es_cliente or user.is_staff:
            print("Usuario existe")
            login(request, user)
            return redirect('paciente')
        elif user is not None and user.es_trabajador:
            print("Usuario existe y es trabajador")
            return redirect('login_trabajador')
        print("Usuario no existe")
# ELIMINAR LOS PRINT



#Esta seccion es para cerrar sesion
def logout_admin(request):
    logout(request)
    return redirect('login_admin')

def logout_PACIENTE(request):
    logout(request)
    return redirect('login_paciente')

def logout_trabajador(request):
    logout(request)
    return redirect('login_trabajador')





def home(request):
    return render(request, 'home.html')

def generar_horas_disponibles():
    inicio = datetime.strptime("09:00", "%H:%M")
    fin = datetime.strptime("18:00", "%H:%M")
    intervalo = timedelta(minutes=45)
    horas = []

    while inicio < fin:
        horas.append(inicio.strftime("%H:%M"))
        inicio += intervalo

    return horas

def pagpedir_hora(request):
    horas_disponibles = generar_horas_disponibles()
    if request.method == 'POST':
        fecha = request.POST.get('fecha_cita')
        hora = request.POST.get('hora_cita')
        # Verificar si la hora ya está reservada
        if Cita.objects.filter(fecha_cita=fecha, hora_cita=hora).exists():
            return render(request, 'pedir_hora.html', {
                'horas_disponibles': horas_disponibles,
                'error': 'Esta hora ya está reservada. Por favor elige otra.'
            })
        # Guardar la cita
        Cita.objects.create(
            nombre_propietario=request.POST.get('nombre_propietario'),
            rut_propietario=request.POST.get('rut_propietario'),
            tipo_mascota=request.POST.get('tipo_mascota'),
            nombre_mascota=request.POST.get('nombre_mascota'),
            fecha_cita=fecha,
            hora_cita=hora,
            propietario=request.user  # Aquí va el usuario que está logueado
        )
        return HttpResponseRedirect('/')
    return render(request, 'pedir_hora.html', {'horas_disponibles': horas_disponibles})

@login_required(login_url="/login_paciente")
def pagpaciente(request):
    return render(request, 'ingreso_paciente.html', {
        'UserVeterinaria': request.user
    })

def pagadmin(request):
    return render(request, 'admin.html')

login_required(login_url="/login_paciente")
def pagrev_hora(request):
    return render(request, 'revision_hora.html')

def pagtrabajadores(request):
    return render(request, 'trabajadores.html', {
        'UserVeterinaria': request.user
        })

# Create your views here.


@login_required(login_url="/login_paciente")
def pagrev_hora(request):
    print("hola")
    citas =  Cita.objects.filter(propietario=request.user)
    print("citas encontradas: ", citas.count()) # O usa otro campo si lo prefieres

    if request.method == 'POST':
        cita_id = request.POST.get('cita_id')
        Cita.objects.filter(id=cita_id).delete()
        return redirect('revisar')

    return render(request, 'revision_hora.html', {'citas': citas})
