from django import forms
from .models import Funcionario



class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'funcao', 'email', 'foto']
        widgets = {
            'nome': forms.TextInput(
            attrs={'class': 'input', 'type': 'text', 'pleaceholder': 'Digite o nome do funcionario'}),
            'funcao': forms.TextInput(
            attrs={'class': 'input', 'type': 'text', 'pleaceholder': 'Digite o funcao do funcionario'}),
            'email': forms.TextInput(
            attrs={'class': 'input',  'pleaceholder': 'Digite o email do funcionario'}),
            'foto': forms.FileInput(attrs={'class':'input', 'type': 'file'}),
    }

    error_messages = {
        'nome': {'required': 'O nome do funcionario e um campo obrigatorio',
                 'unique': 'Funcionario ja cadastrado'},
        'endereco': {'required': 'O endereco do funcionario e um campo obrigatorio'},
        'email': {'required': 'O email e um campo obrigatorio',
                      'invalid': 'Formato invalido para o e-mail. Exemplo de formato válido: fulano@dominio.com',
                      'unique': 'E-mail já cadastrado'},
    }