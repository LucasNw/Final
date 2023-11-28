from django.db import models

from django.db import models
from home.models import Pessoa


class Funcionario(Pessoa):
    funcao = models.CharField('Função', max_length=100, help_text= 'Função na empresa')


    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return super().nome