from django import forms
from .models import Usuario

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'email', 'foto']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'pleaceholder': 'Digite o nome do usuario'}),
            'endereco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'pleaceholder': 'Digite o endereco do usuario'}),
            'email': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'pleaceholder': 'Digite o numero do usuario'}),
            'foto': forms.FileInput(attrs={'class':'input', 'type': 'file'}),
        }

        error_messages = {
            'nome': {'required': 'O nome do usuario e um campo obrigatorio'},
            'endereco': {'required': 'O endereco do usuario e um campo obrigatorio'},
            'email': {'required': 'O email e um campo obrigatorio',
                      'invalid': 'Formato invalido para o e-mail. Exemplo de formato válido: fulano@dominio.com',
                      'unique': 'E-mail já cadastrado'},
        }