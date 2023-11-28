from django.db import models
from home.models import Pessoa


class Usuario(Pessoa):
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço completo')


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome


