from django.db import models


class Aula(models.Model):
    nome = models.CharField(max_length=60)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
