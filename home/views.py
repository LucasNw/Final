from django.views.generic import TemplateView

from chave.models import Chave
from entrega.models import Entrega
from funcionario.models import Funcionario
from sala.models import Sala
from usuario.models import Usuario


class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self):
        context = super(IndexView, self). get_context_data()
        context['qtd_usuarios'] = Usuario.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_chaves'] = Chave.objects.count()
        context['qtd_salas'] = Sala.objects.count()
        context['qtd_entregas'] = Entrega.objects.count()
        return context
