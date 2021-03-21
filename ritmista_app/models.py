from django.db import models
from datetime import datetime


class Grupo(models.Model):
    grupo = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):
        return self.grupo


class Naipe(models.Model):
    naipe = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.naipe


class Curso(models.Model):
    curso = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.curso


class Ritmista(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False, db_column='Nome')
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, default=None, db_column='Curso')
    naipe = models.ForeignKey(Naipe, on_delete=models.DO_NOTHING, default=None, db_column='Naipe')
    grupo = models.ManyToManyField(Grupo, blank=False, db_column='Grupo', default=None)
    data_entrada = models.DateField(blank=False, null=False,
                                    db_column='Data de entrada', verbose_name='Data de entrada')
    data_nascimento = models.DateField(blank=False, null=False, db_column='Data de nascimento',
                                       verbose_name='Data de nascimento', default=None)
    cpf = models.CharField(max_length=11, blank=False, null=False,
                           db_column='CPF', verbose_name='CPF', unique=True, default=None)
    telefone = models.CharField(max_length=11, blank=False, null=False,
                                db_column='Telefone', default=None)
    data_saida = models.DateField(blank=True, null=True,
                                  db_column='Data de saída', verbose_name='Data de saída')

    def __str__(self):
        return self.nome
