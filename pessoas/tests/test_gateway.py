from django.test import TestCase

from pessoas.gateway import busca_pessoas_nao_excluidas, busca_uma_pessoa, criar_pessoa, alterar_pessoa
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


class CriarPessoaTests(TestCase):

    def test_gera_erro_ao_criar_pessoa_sem_nome(self):
        nome = ''
        idade = 18

        with self.assertRaises(Exception) as contexto:
            criar_pessoa(nome, idade)

        self.assertEqual('É necessário informar o nome!', str(contexto.exception))

    def test_gera_erro_ao_criar_pessoa_com_idade_invalida(self):
        nome = 'João'
        idade = 200

        with self.assertRaises(Exception) as contexto:
            criar_pessoa(nome, idade)

        self.assertEqual('Informe uma idade maior ou igual a zero!', str(contexto.exception))

    def test_cria_uma_pessoa_completa(self):
        nome = 'Jorge'
        idade = 33

        pessoa = criar_pessoa(nome, idade)

        pessoa_encontrada = Pessoa.objects.get(id=pessoa.id)
        self.assertEqual(nome, pessoa_encontrada.nome)
        self.assertEqual(idade, pessoa_encontrada.idade)
        self.assertIsNotNone(pessoa_encontrada.ultima_alteracao)
        self.assertFalse(pessoa_encontrada.excluido)


class AlterarPessoaTests(TestCase):

    def test_gera_arro_quando_altera_uma_pessoa_passando_nome_vazio(self):
        pessoa = Pessoa.objects.create(nome='João', idade=18)

        with self.assertRaises(Exception) as contexto:
            alterar_pessoa(pessoa.id, nome='', idade=18)

        self.assertEqual('É necessário informar o nome!', str(contexto.exception))

    def test_gera_arro_quando_altera_uma_pessoa_passando_idade_invalida(self):
        pessoa = Pessoa.objects.create(nome='João', idade=18)

        with self.assertRaises(Exception) as contexto:
            alterar_pessoa(pessoa.id, nome='João', idade=200)

        self.assertEqual('Informe uma idade maior ou igual a zero!', str(contexto.exception))

    def test_altera_uma_pessoa_com_sucesso(self):
        pessoa = Pessoa.objects.create(nome='João', idade=18)
        novo_nome = 'Jorge'
        nova_idade = 33

        alterar_pessoa(pessoa.id, nome=novo_nome, idade=nova_idade)

        pessoa_encontrada = Pessoa.objects.get(id=pessoa.id)
        self.assertEqual(novo_nome, pessoa_encontrada.nome)
        self.assertEqual(nova_idade, pessoa_encontrada.idade)
        self.assertFalse(pessoa_encontrada.excluido)
