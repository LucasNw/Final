from django.urls import path
from .views import IndexView
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', extra_context={'titulo':'Autenticação'}), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),
    path('alterar_senha/', auth_views.PasswordChangeView.as_view(template_name='login.html', extra_context={'titulo': 'Alterar senha'},
        success_url=reverse_lazy('index')), name="alterar_senha"),
]