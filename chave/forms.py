from django import forms


from .models import Chave

class ChaveModelForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = ['sala', 'numCopia', 'status']


        error_messages = {
            'sala': {'required': 'O nome do produto e um campo obrigatorio',
                    'unique': 'Sala ja cadastrada'},
            'numCopia': {'required': 'Informe o quantas copias a chave tem'},
            'status':{'required': 'Infome o status da chave'}

        }