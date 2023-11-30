from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from funcionario.forms import FuncionarioModelForm
from funcionario.models import Funcionario


class FuncionariosView(PermissionRequiredMixin, ListView):
    permission_required = 'funcionario.view_funcionario'
    permission_denied_message = 'Ver Funcionario'
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem funcionarios cadastrados!")


class FuncionarioAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'funcionario.add_funcionario'
    permission_denied_message = 'Cadastrar Funcionario'
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario cadastrado com sucesso'


class FuncionarioUpDateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'funcionario.change_funcionario'
    permission_denied_message = 'Alterar Funcionario'
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario atualizado com sucesso'


class FuncionarioDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'funcionario.delete_funcionario'
    permission_denied_message = 'Deletar Funcionario'
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario excluido com sucesso'
