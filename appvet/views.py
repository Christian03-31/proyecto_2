from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout




#Esta seccion es para iniciar sesion
def login_admin(request):
    return redirect(request, '/admin')



def login_trabajador(request):
    if request.method == 'GET':
        print("GET")
        return render(request, 'logins/login_trabajador.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('login_trabajador')
    return render(request, 'logins/login_trabajador.html')



def login_paciente(request):
    if request.method == 'GET':
        print("GET")
        return render(request, 'logins/login_paciente.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print("Usuario existe")
            login(request, user)
            return redirect('paciente')
        print("Usuario no existe")
        return render(request, 'logins/login_paciente.html')
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

def pagpedir_hora(request):
    return render(request, 'pedir_hora.html')

def pagpaciente(request):
    return render(request, 'ingreso_paciente.html')

def pagadmin(request):
    return render(request, 'admin.html')

def pagrev_hora(request):
    return render(request, 'revision_hora.html')

def pagtrabajadores(request):
    return render(request, 'trabajadores.html')

# Create your views here.
