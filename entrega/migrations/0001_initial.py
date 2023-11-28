# Generated by Django 4.2.5 on 2023-11-17 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0002_alter_usuario_email'),
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(help_text='Data e hora do atendimento', verbose_name='Horario')),
                ('sala', models.ForeignKey(help_text='Local da sala', on_delete=django.db.models.deletion.CASCADE, to='sala.sala', verbose_name='Sala')),
                ('usuario', models.ForeignKey(help_text='Nome do cliente', on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]