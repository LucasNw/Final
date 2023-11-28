from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import SalaModelForm
from sala.models import Sala



class SalaView(ListView):
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



class SalaAddView(CreateView):
    form_class = SalaModelForm
    model = Sala
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')

class SalaUpDateView(UpdateView):
    form_class = SalaModelForm
    model = Sala
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')

class SalaDeleteView(DeleteView):
    model = Sala
    template_name = 'sala_apagar.html'
    success_url = reverse_lazy('salas')


