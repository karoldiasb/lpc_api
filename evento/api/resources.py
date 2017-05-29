from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from evento.models import *
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized

class TipoInscricaoResource(ModelResource):
    def obj_create(self,bundle,**kwargs): #bundle é o objeto
        print(bundle.data) #bundle.data acessa o dado dentro do objeto, que no caso é a descricao
        tipo = TipoInscricao()
        if not (TipoInscricao.objects.filter(descricao=bundle.data['descricao'])):
            tipo.descricao = bundle.data['descricao'].upper()
            tipo.save()
            bundle.obj = tipo
            return bundle
        else:
            raise Unauthorized('Já existe tipo com esse nome');

    def obj_delete_list(self,bundle,**kwargs):
        raise Unauthorized('Você não pode deletar essa lista');

    class Meta:
        queryset = TipoInscricao.objects.all() #lista ou consulta do recurso
        allowed_methods = ['get','post','put','delete']
        filtering = { #aplicações de filtros, recebe um json
            "descricao": ('exact', 'startswith',) #o campo descrição é para fornecer dois tipos de filtros, passando a palavra exata e um tipo de filtro
        }
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']
        authorization = Authorization() #permite que qualquer pessoa faça requisições (chamadas) para APIS (chamadas Put)

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class EventoResource(ModelResource):
    realizador  = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post','put','delete'] #tipos de métodos
        authorization = Authorization()

class EventoCientificoResource(ModelResource):
    realizador  = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "titulo": ('exact', 'startswith',)
        }
        authorization = Authorization()

class InscricoesResource(ModelResource):
    def obj_create(self, bundle, **kwargs):

        pessoa = bundle.data['pessoa'].split("/")
        evento = bundle.data['evento'].split("/")
        tipoInsc = bundle.data['tipoInscricao'].split("/")

        oi = Inscricoes.objects.filter(pessoa=pessoa[4], evento=evento[4])
        if oi.count() > 0:
            raise Unauthorized('Já existe inscrição com essa pessoa');

        else:
            tipo = Inscricoes()

            tipo.pessoa = PessoaFisica.objects.get(pk=pessoa[4])
            tipo.evento = Evento.objects.get(pk=evento[4])
            tipo.tipoInscricao = TipoInscricao.objects.get(pk=tipoInsc[4])
            tipo.save()
            bundle.obj = tipo
            return bundle


    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()
        filtering = {
            "tipoInscricao": ('exact', 'startswith',)
        }

class ArtigoAutorResource(ModelResource):
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get','post','put','delete']
        authorization = Authorization()
