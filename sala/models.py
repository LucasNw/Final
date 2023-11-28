from django.db import models


class Sala(models.Model):
    tipoSala = models.CharField('Tipo', max_length=50, help_text='Tipo da sala', unique=False)
    local = models.CharField('Local', max_length=50, help_text='Local da sala', unique=False)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return self.local
