from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


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
    listaMateria=["HTML", "CSS", "JS","DJANGO","PYTHON"]
    context={"nombre" : "Gabriel muñoz", "Materia" : listaMateria}
            
    return render(request,'index.html',context)