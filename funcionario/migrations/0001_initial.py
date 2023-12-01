# Generated by Django 4.2.5 on 2023-12-01 17:09

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo', max_length=50, verbose_name='Nome')),
                ('email', models.CharField(help_text='Numero de Telefone', max_length=15, verbose_name='Email')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={}, verbose_name='Foto')),
                ('funcao', models.CharField(help_text='Função na empresa', max_length=100, verbose_name='Função')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
