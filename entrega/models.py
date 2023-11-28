from django.db import models

class Entrega(models.Model):
    horario = models.DateTimeField('Horario', help_text='Data e hora do atendimento')
    usuario = models.ForeignKey('usuario.Usuario', verbose_name='Usuario' ,help_text='Nome do cliente',
                                on_delete=models.CASCADE)
    sala = models.ForeignKey('sala.Sala', verbose_name='Sala', help_text='Local da sala',
                                on_delete=models.CASCADE)




    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'


    def __str__(self):
        return f'Usuario: {self.usuario} - Sala:{self.sala} - Horiario:{self.horario}'
