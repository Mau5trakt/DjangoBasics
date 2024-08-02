from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(' <h1> Este es el index <h1>')


def wilmer(request):
    return HttpResponse('<h1 style="color: blue;"> Hola Mundito </h1>')


def saludo(request, nombre):
    return HttpResponse(f'<h1> Hola {nombre}')

def tichers(request):
    profesores = [
        {
            'id': 1,
            "nombre": "Wilmer Edmundo Umaña",
            "edad": 20,
            "carrera": "Ingeniería en Computación",
            "horario": '10:00 - 12:00'
        },
        {
            'id': 2,
            "nombre": "Enrique Mauricio Alemany",
            "edad": 23,
            "carrera": "Ingeniería Química",
            "horario": '10:00 - 12:00'
        }
    ]

    return JsonResponse(profesores, safe=False)