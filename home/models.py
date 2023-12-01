from django.db import models
from stdimage import StdImageField


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length = 50, help_text = 'Nome completo')
    email = models.EmailField('Email', max_length=100, help_text='Numero de Telefone')
    foto = StdImageField('Foto', upload_to='pessoas', delete_orphans=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome