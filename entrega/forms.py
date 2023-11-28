from django import forms


from entrega.models import Entrega
from sala.models import Sala
from usuario.models import Usuario

class EntregaListForm(forms.Form):
    usuario = forms.ModelChoiceField(label='Usuario:', widget=forms.Select(
            attrs={'class': 'select is-fullwidth'}), queryset=Usuario.objects.all(), required=False)

    sala = forms.ModelChoiceField(label='Sala:', widget=forms.Select(
        attrs={'class': 'select is-fullwidth'}), queryset=Sala.objects.all(), required=False)


class EntregaModelForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['horario', 'usuario', 'sala']

        error_messages = {
            'horario': {'required': 'O horario e um campo obrigatorio'},
            'usuario': {'required': 'O usuario e um campo obrigatorio'},
            'sala': {'required': 'A sala  e um campo obrigatorio'}
        }
