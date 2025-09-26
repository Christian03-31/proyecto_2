from django.shortcuts import render

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
