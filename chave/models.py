from django.db import models

class Chave(models.Model):
    STATUS = (
        ('E', 'Em uso'),
        ('L', 'Livre'),
    )

    sala = models.ForeignKey('sala.Sala', verbose_name='Sala', on_delete=models.CASCADE, related_name='sala')
    numCopia = models.CharField('Numero de Copia', max_length=20, default=0)
    status = models.CharField('Status da Chave', max_length=20, choices=STATUS, default='L')


    class Meta:
        verbose_name = 'Chave utilizada'
        verbose_name_plural = 'Chaves utilizadas'


    def __str__(self):
        return self.numCopia
