from django.test import TestCase

from pessoas.gateway import busca_pessoas_nao_excluidas, busca_uma_pessoa
from pessoas.models import Pessoa


class BuscaPessoasNaoExcluidasTests(TestCase):

    def test_nao_busca_pessoas_excluidas(self):
        Pessoa.objects.create(idade=18, excluido=True)

        pessoas = busca_pessoas_nao_excluidas()

        self.assertEqual(0, len(pessoas))

    def test_deve_encontrar_pessoas_nao_excluidas(self):
        Pessoa.objects.create(idade=18, excluido=True)
        Pessoa.objects.create(idade=18, excluido=False)

        pessoas = busca_pessoas_nao_excluidas()

        self.assertEqual(1, len(pessoas))


class BuscaUmaPessoaTests(TestCase):

    def test_gera_erro_quando_nao_encontra_a_pessoa(self):
        with self.assertRaises(Pessoa.DoesNotExist):
            busca_uma_pessoa(1)

    def test_deve_encontrar_pessoa_por_id(self):
        pessoa = Pessoa.objects.create(nome='João', idade=18, excluido=False)

        pessoa_encontrada = busca_uma_pessoa(pessoa.id)

        self.assertEqual('João', pessoa_encontrada.nome)
        self.assertEqual(18, pessoa_encontrada.idade)
        self.assertFalse(pessoa_encontrada.excluido)
        self.assertIsNotNone(pessoa_encontrada.id)
