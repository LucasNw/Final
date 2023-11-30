from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from usuario.forms import UsuarioModelForm
from usuario.models import Usuario


# Create your views here.
class UsuariosView(PermissionRequiredMixin, ListView):
    permission_required = 'usuario.view_usuario'
    permission_denied_message = 'Ver usuario'
    model = Usuario
    template_name = 'usuarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(UsuariosView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem usuarios cadastrados!")


class UsuarioAddView(SuccessMessageMixin, CreateView):
    permission_required = 'usuario.add_usuario'
    permission_denied_message = 'Cadastrar usuario'
    form_class = UsuarioModelForm
    model = Usuario
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuarios')
    success_message = 'Usuario cadastrado com sucesso'



class UsuarioUpDateView(SuccessMessageMixin, UpdateView):
    permission_required = 'usuario.change_usuario'
    permission_denied_message = 'Alterar usuario'
    form_class = UsuarioModelForm
    model = Usuario
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuarios')
    success_message = 'Usuario alterado com sucesso'


class UsuarioDeleteView(SuccessMessageMixin, DeleteView):
    permission_required = 'usuario.delete_usuario'
    permission_denied_message = 'Deletar usuario'
    model = Usuario
    template_name = 'usuario_apagar.html'
    success_url = reverse_lazy('usuarios')
    success_message = 'Usuario excluido com sucesso'
