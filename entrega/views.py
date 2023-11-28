from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib import messages
import sala
import usuario
from entrega.forms import EntregaListForm, EntregaModelForm
from entrega.models import Entrega


class EntregaView(ListView):
    model = Entrega
    template_name = 'entregas.html'

    def get_context_data(self, **kwargs):
        context = super(EntregaView, self).get_context_data(**kwargs)
        if self.request.GET:
            form = EntregaListForm(self.request.GET)
        else:
            form = EntregaListForm()
        context['form'] = form
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(EntregaView,self).get_queryset()
        if self.request.GET:
            form = EntregaListForm(self.request.GET)
            if form.is_valid():
                usuario = form.cleaned_data.get('usuario')
                sala = form.cleaned_data.get('sala')
                if usuario:
                    qs = qs.filter(usuario=usuario)
                if sala:
                    qs = qs.filter(sala=sala)
        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem entregas cadastrados")



class EntregaAddView(SuccessMessageMixin, CreateView):
    form_class = EntregaModelForm
    model = Entrega
    template_name = 'entrega_form.html'
    success_url = reverse_lazy('entregas')
    success_message = 'Entrega cadastrada com sucesso'

class EntregaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = EntregaModelForm
    model = Entrega
    template_name = 'entrega_form.html'
    success_url = reverse_lazy('entregas')
    success_message = 'Entrega cadastrada com sucesso'

class EntregaDeleteView(SuccessMessageMixin, DeleteView):
    model = Entrega
    template_name = 'entrega_apagar.html'
    success_url = reverse_lazy('entregas')
    success_message = 'Entrega cadastrada com sucesso'

class EntregaExibir(DetailView):
    model = Entrega
    template_name = 'entrega_exibir.html'

    def get_object(self, queryset=None):
        entrega = Entrega.objects.get(pk=self.kwargs.get('pk'))
        self.enviar_email(entrega)
        return entrega


    def enviar_email(self, entrega):
        email = []
        email.append(entrega.usuario.email)


        dados = {'usuario': entrega.usuario.nome,
                 'horario': entrega.horario,
                 'sala': entrega.sala, }

        texto_email = render_to_string('emails/texto_email.txt', dados)
        html_email = render_to_string('emails/texto_email.html', dados)
        send_mail(subject='Agenda - Serviço concluido',
                  message=texto_email,
                  from_email='lucas.leitemperguer@gmail.com',
                  recipient_list=email,
                  html_message=html_email,
                  fail_silently=False
                  )

        return redirect('entregas')
