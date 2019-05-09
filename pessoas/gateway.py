# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime

from pessoas.models import Pessoa


def busca_pessoas_nao_excluidas():
    return Pessoa.objects.filter(excluido=False)


def busca_uma_pessoa(pessoa_id):
    return Pessoa.objects.get(id=pessoa_id)


def criar_pessoa(nome, idade):
    pessoa = Pessoa()
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.ultima_alteracao = datetime.now()
    pessoa.save()
    return pessoa


def alterar_pessoa(pessoa_id, nome, idade):
    pessoa = busca_uma_pessoa(pessoa_id)
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.ultima_alteracao = datetime.now()
    pessoa.save()


def excluir_pessoa(pessoa_id):
    pessoa = busca_uma_pessoa(pessoa_id)
    pessoa.excluido = True
    pessoa.ultima_alteracao = datetime.now()
    pessoa.save()
