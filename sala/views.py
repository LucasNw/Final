from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import SalaModelForm
from sala.models import Sala



class SalaView(PermissionRequiredMixin, ListView):
    permission_required = 'sala.view_sala'
    permission_denied_message = 'Ver sala'
    model = Sala
    template_name = 'sala.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(SalaView, self).get_queryset()
        if buscar:
            qs = qs.filter(tipoSala__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não exixtem produtos cadastrados!")



class SalaAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'sala.add_sala'
    permission_denied_message = 'Cadastrar sala'
    form_class = SalaModelForm
    model = Sala
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')

class SalaUpDateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'sala.change_sala'
    permission_denied_message = 'Alterar sala'
    form_class = SalaModelForm
    model = Sala
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')

class SalaDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'sala.delete_sala'
    permission_denied_message = 'Deletar sala'
    model = Sala
    template_name = 'sala_apagar.html'
    success_url = reverse_lazy('salas')


