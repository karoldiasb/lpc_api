"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from tastypie.api import Api
from django.contrib import admin
from evento.api.resources import TipoInscricaoResource, UserResource, PessoaResource

from evento.views import *

v1_api = Api(api_name='v1')
v1_api.register(TipoInscricaoResource())
v1_api.register(UserResource())
v1_api.register(PessoaResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^eventos/', listaEventos, name='listaEventos'),
    url(r'^evento/([0-9]{1})', eventoid, name='eventoId'),
    url(r'^eventoscientificos/', listaEventoCientifico, name='listaEventoCientifico'),
    url(r'^eventocientifico/([0-9]{1})/', eventoCientificoid, name='eventoCientificoid'),
    url(r'^pessoas/', listaPessoas, name='listaPessoas'),
    url(r'^pessoa/([0-9]{1})/',pessoaid, name='pessoaid'),
    url(r'^pessoasfisicas/', listaPessoasFisicas, name='listaPessoasFisicas'),
    url(r'^pessoafisica/([0-9]{1})', pessoaFisicaid, name='pessoaFisicaid'),
    url(r'^pessoasjuridicas/', listaPessoasJuridicas, name='listaPessoasJuridicas'),
    url(r'^pessoajuridica/([0-9]{1})', pessoaJuridicaid, name='pessoaJuridicaid'),
    url(r'^autores/', listaAutores, name='listaAutores'),
    url(r'^autor/([0-9]{1})', autorid, name='autorid'),
    url(r'^artigoscientificos/', listaArtigosCientificos, name='listaArtigosCientificos'),
    url(r'^artigocientifico/([0-9]{1})', artigocientificoid, name='artigocientificoid'),
    url(r'^eventoinscricoes/([0-9]{1})', listainscricoes, name='listainscricoes'),
    url(r'^api/', include(v1_api.urls)),
]
