from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mascota, Sexo


# Create your views here.
def primerSaludo(request):
    return HttpResponse("Feliz Cumpleaños tonto leso");

def mostrarNombre(request,nombre):
    documentoHTML="""
    <html>
        <head></head>
        <body>
            <h1> Se ha ingresado a: %s</h1>
        </body>
    </html>"""%nombre
    return HttpResponse(documentoHTML)

def index(request):
    mascotas=Mascota.objecs.all()
    context=('mascotas' Mascota)
            
    return render(request,'index.html',context)