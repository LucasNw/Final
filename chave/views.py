from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ChaveModelForm
from chave.models import Chave



class ChaveView(ListView):
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


class ChaveAddView(CreateView):
    form_class = ChaveModelForm
    model = Chave
    template_name = 'chave_form.html'
    success_url = reverse_lazy('chaves')

class ChaveUpDateView(UpdateView):
    form_class = ChaveModelForm
    model = Chave
    template_name = 'chave_form.html'
    success_url = reverse_lazy('chaves')

class ChaveDeleteView(DeleteView):
    model = Chave
    template_name = 'chave_apagar.html'
    success_url = reverse_lazy('chaves')

