from django.urls import path

from .views import EntregaView, EntregaAddView, EntregaUpDateView, EntregaDeleteView, EntregaExibir

urlpatterns = [
    path('entregas', EntregaView.as_view(), name='entregas'),
    path('entrega/adicionar/', EntregaAddView.as_view(), name='entrega_adicionar'),
    path('<int:pk>/entrega/editar/', EntregaUpDateView.as_view(), name='entrega_editar'),
    path('<int:pk>/entrega/apagar/', EntregaDeleteView.as_view(), name='entrega_apagar'),
    path('<int:pk>/entrega/exibir/', EntregaExibir.as_view(), name='entrega_exibir'),

]