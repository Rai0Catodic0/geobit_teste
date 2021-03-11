from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    autor = models.ForeignKey('Autor',on_delete=models.CASCADE)
    quantidade_de_paginas = models.IntegerField()
    preco = models.FloatField()
    data_de_inclusao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome