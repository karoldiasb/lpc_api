from tastypie.resources import ModelResource
from evento.models import TipoInscricao, Pessoa
from django.contrib.auth.models import User


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get']


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get']
        resource_name = 'P'
