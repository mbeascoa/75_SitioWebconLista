from django.shortcuts import render
from formulario.models import Cliente


def index(request):
     return render(request, "deportes/Inicio.html")

def formulario(request):
    nombre = request.POST['nombre']
    ape1 = request.POST['apellido1']
    ape2 = request.POST['apellido2']
    domi = request.POST['domicilio']
    ciud = request.POST['ciudad']
    sx = request.POST['sexo']
    com = request.POST['comentarios']

    datos = request.POST.getlist('so')

    cadena=""
    for a in datos:
        cadena=cadena+a+","

    # Quitamos la última coma de la cadena.
    # Desde la primera posición hasta la última -1
    # EJEMPLO: Obtenemos la subcadena desde el principio hasta la posición 10. subcadena = cadena[:10]
    datosSO=cadena[:len(cadena)-1]

    clte = Cliente()
    numeroReg=clte.altaCliente(nombre,ape1,ape2,domi,ciud,sx,datosSO,com)
    contexto = {
        'resultado': numeroReg
    }
    return render(request, "deportes/Inicio.html", contexto)