
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.url.home_urls')),
    path(
        'catalogo/',
        RedirectView.as_view(pattern_name='home', permanent=False),
        name='catalogo',
    ),
    path('catalogo/',
         include('catalogo.url.categoria_urls')),
    path('catalogo/',
         include('catalogo.url.libro_urls')),
]