from django.http import JsonResponse
from  django.shortcuts import render


# Retorna alunos json
def alunos(request):
    if (request.method == 'GET'):
        alunos = {'id': 1, 'name': 'Joao'}
        return JsonResponse(alunos)