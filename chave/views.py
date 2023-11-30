from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ChaveModelForm
from chave.models import Chave



class ChaveView(PermissionRequiredMixin, ListView):
    permission_required = 'chave.view_chave'
    permission_denied_message = 'Vizualizar Chave'
    model = Chave
    template_name = 'chave.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ChaveView, self).get_queryset()
        if buscar:
            qs = qs.filter(numCopia__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não exixtem chaves cadastrados!")


class ChaveAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'chave.add_chave'
    permission_denied_message = 'Cadastrar Chave'
    form_class = ChaveModelForm
    model = Chave
    template_name = 'chave_form.html'
    success_url = reverse_lazy('chaves')

class ChaveUpDateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'chave.change_chave'
    permission_denied_message = 'Editar Chave'
    form_class = ChaveModelForm
    model = Chave
    template_name = 'chave_form.html'
    success_url = reverse_lazy('chaves')

class ChaveDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'chave.delete_chave'
    permission_denied_message = 'Deletar Chave'
    model = Chave
    template_name = 'chave_apagar.html'
    success_url = reverse_lazy('chaves')

