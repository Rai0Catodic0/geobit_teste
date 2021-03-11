from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core import serializers
from .models import Livro, Autor
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
import datetime


# Create your views here.
@api_view(["GET"])
def get_livros(request):
    livros = Livro.objects.all()
    return JsonResponse({'livros': serializers.serialize('json',livros)},safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_livro(request):
    payload = json.loads(request.body)
    try:
        autor = Autor.objects.get(nome=payload["autor"])
    except ObjectDoesNotExist:
        autor = Autor.objects.create(nome=payload["autor"])
    
    livro = Livro.objects.create(
        nome = payload["nome"],
        autor = autor,
        quantidade_de_paginas = payload["quantidade_de_paginas"],
        preco= payload["preco"]
    )
    livro = Livro.objects.filter(nome=payload["nome"])
    return JsonResponse({'livros':serializers.serialize("json",livro)},safe=False, status = status.HTTP_201_CREATED)

@api_view(["PUT"])
def update_livro(request, id_livro):
    payload = json.loads(request.body)
    try:
        livro = Livro.objects.filter(id=id_livro)
        livro.update(**payload)
        livro = Livro.objects.filter(id=id_livro)
        livro = serializers.serialize('json', livro)
        return JsonResponse({'book': livro}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        