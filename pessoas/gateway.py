from datetime import datetime

from django.utils import timezone

from pessoas.models import Pessoa


def busca_pessoas_nao_excluidas():
    return Pessoa.objects.filter(excluido=False)


def busca_uma_pessoa(pessoa_id):
    return Pessoa.objects.get(id=pessoa_id)


def criar_pessoa(nome, idade):
    if not nome:
        raise Exception('É necessário informar o nome!')

    if idade < 0 or idade > 150:
        raise Exception('Informe uma idade maior ou igual a zero!')

    pessoa = Pessoa()
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.ultima_alteracao = timezone.now()
    pessoa.save()
    return pessoa


def alterar_pessoa(pessoa_id, nome, idade):
    if not nome:
        raise Exception('É necessário informar o nome!')

    if idade < 0 or idade > 150:
        raise Exception('Informe uma idade maior ou igual a zero!')

    pessoa = busca_uma_pessoa(pessoa_id)
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.ultima_alteracao = timezone.now()
    pessoa.save()
    return pessoa


def excluir_pessoa(pessoa_id):
    pessoa = busca_uma_pessoa(pessoa_id)
    pessoa.excluido = True
    pessoa.ultima_alteracao = timezone.now()
    pessoa.save()
