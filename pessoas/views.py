from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from pessoas.forms import FormPessoa
from pessoas.gateway import busca_pessoas_nao_excluidas, busca_uma_pessoa, criar_pessoa, alterar_pessoa, excluir_pessoa


class ListarPessoasView(View):
    def get(self, request):
        pessoas = busca_pessoas_nao_excluidas()
        return render(request, 'listar_pessoas.html', {'pessoas': pessoas})


class CadastrarPessoaView(View):
    def get(self, request):
        form = FormPessoa()
        return render(request, 'cadastrar_pessoa.html', {'form': form})

    def post(self, request):
        form = FormPessoa(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_pessoa.html', {'form': form})

        nome = form.cleaned_data['nome']
        idade = form.cleaned_data['idade']

        criar_pessoa(nome, idade)

        return redirect(reverse('listar_pessoas'))


class AlterarPessoaView(View):
    def get(self, request, pessoa_id=None):
        pessoa = busca_uma_pessoa(pessoa_id)
        form = FormPessoa(initial={'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade})
        return render(request, 'alterar_pessoa.html', {'form': form, 'pessoa_id': pessoa_id})

    def post(self, request, pessoa_id=None):
        form = FormPessoa(request.POST)

        if not form.is_valid():
            return render(request, 'alterar_pessoa.html', {'form': form, 'pessoa_id': pessoa_id})

        nome = form.cleaned_data['nome']
        idade = form.cleaned_data['idade']

        alterar_pessoa(pessoa_id, nome, idade)

        return redirect(reverse('listar_pessoas'))


class ExcluirPessoaView(View):
    def get(self, request, pessoa_id=None):
        pessoa = busca_uma_pessoa(pessoa_id)
        return render(request, 'confirma_excluir_pessoa.html', {'pessoa_id': pessoa_id, 'nome': pessoa.nome})

    def post(self, request, pessoa_id=None):
        excluir_pessoa(pessoa_id)

        return redirect(reverse('listar_pessoas'))
