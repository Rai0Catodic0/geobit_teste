from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import LivroSerializer
from .models import Livro, Autor
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
import datetime


# Create your views here.
@api_view(["GET"])
def get_livros(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)
    return JsonResponse({'livros': serializer.data},safe=False, status=status.HTTP_200_OK)


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
    serializer = LivroSerializer(livro)
    return JsonResponse({'livros':serializer.data},safe=False, status = status.HTTP_201_CREATED)

    