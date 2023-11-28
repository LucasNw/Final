
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('sala.urls')),
    path('', include('usuario.urls')),
    path('', include('funcionario.urls')),
    path('', include('chave.urls')),
    path('', include('entrega.urls')),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


