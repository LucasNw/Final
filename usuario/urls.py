from django.urls import path
from .views import UsuariosView, UsuarioAddView, UsuarioUpDateView, UsuarioDeleteView

urlpatterns = [
    path('usuarios', UsuariosView.as_view(), name='usuarios'),
    path('usuario/adicionar/', UsuarioAddView.as_view(), name='usuario_adicionar'),
    path('<int:pk>/usuario/editar/', UsuarioUpDateView.as_view(), name='usuario_editar'),
    path('<int:pk>/usuario/apagar/', UsuarioDeleteView.as_view(), name='usuario_apagar')

]