from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    autor = models.ForeignKey('Autor',on_delete=models.CASCADE)
    quantidade_de_paginas = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    preco = models.FloatField(validators=[MinValueValidator(0)])
    data_de_inclusao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome