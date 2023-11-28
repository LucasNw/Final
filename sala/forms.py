from django import forms
from django.forms import inlineformset_factory

from .models import Sala

class SalaModelForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['tipoSala', 'local',]


        error_messages = {
            'local da sala': {'required': 'O nome do produto e um campo obrigatorio',
                    'unique': 'Produto ja cadastrado'},
            'tipo da sala': {'required': 'O endereco do cliente e um campo obrigatorio'},

        }